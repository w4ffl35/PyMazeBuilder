from typing import Optional

from pymazebuilder.generators.generator import Generator


class StairsGenerator(Generator):
    def __init__(
        self,
        data: Optional[dict] = None,
        ascending: bool = False,
        max_stairs: int = 1,
        floors: Optional[int] = None,
        current_floor: int = 0,
        previous_floor_data: Optional[dict] = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.data = data or {}
        self.ascending = ascending
        self.max_stairs = max_stairs
        self.floors = floors
        self.current_floor = current_floor
        self.previous_floor_data = previous_floor_data
        self.stairs_locations_by_floor = {}  # Dictionary to track stairs locations by floor
        self.generate()

    def generate(self):
        total_stairs = 0
        while total_stairs < self.max_stairs:
            if self.previous_floor_data:
                prev_stairs = self.previous_floor_data['stairs_down']
                cell = self.data['grid'].get_cell(prev_stairs['x'], prev_stairs['y'], self.current_floor)
                if cell.blocked or cell.stairs:
                    continue
                cell.stairs = {'direction': 'down' if self.ascending else 'up'}
                self.stairs_locations_by_floor[self.current_floor] = []
                self.stairs_locations_by_floor[self.current_floor].append({'x': cell.x, 'y': cell.y})
                total_stairs += 1
                break

            cell = self.data['grid'].random_cell()
            if cell.blocked or cell.stairs:
                continue

            cell.stairs = {'direction': 'up' if self.ascending else 'down'}
            self.stairs_locations_by_floor[self.current_floor] = []
            self.stairs_locations_by_floor[self.current_floor].append({'x': cell.x, 'y': cell.y})
            total_stairs += 1

            self.data['grid'].cells[cell.y][cell.x] = cell
