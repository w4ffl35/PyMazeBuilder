from typing import Optional

from pymazebuilder.generators.generator import Generator


class StairsGenerator(Generator):
    def __init__(
        self,
        data:Optional[dict]=None,
        ascending:bool=False,
        max_stairs:int=1
    ):
        self.data = data or {}
        self.ascending = ascending
        self.max_stairs = max_stairs
        self.generate()

    def generate(self):
        total_stairs_by_floor = {}
        for floor in range(self.data['grid'].total_floors - 1):
            cell = None
            while True:
                if floor in total_stairs_by_floor and total_stairs_by_floor[floor] >= self.max_stairs:
                    break
                previous_floor_cell = None
                next_floor_cell = None

                cell = self.data['grid'].random_cell(floor)
                if cell.blocked:
                    continue

                if floor > 0:
                    previous_floor_cell = self.data['grid'].cells[floor - 1][cell.y][cell.x]
                    if previous_floor_cell.blocked or previous_floor_cell.stairs:
                        previous_floor_cell = None

                next_floor_cell = self.data['grid'].cells[floor + 1][cell.y][cell.x]
                if next_floor_cell is None or next_floor_cell.blocked or next_floor_cell.stairs:
                    continue

                cell.stairs = {
                    'next_floor': next_floor_cell,
                    'direction': 'up' if self.ascending else 'down'
                }
                if next_floor_cell:
                    next_floor_cell.stairs = {
                        'previous_floor': cell,
                        'direction': 'down' if self.ascending else 'up'
                    }
                total_stairs_by_floor[floor] = total_stairs_by_floor.get(floor, 0) + 1
