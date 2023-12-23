class StairsGenerator:
    def __init__(self, data, options):
        self.data = data or {}
        self.options = options or {'ascending': False}
        self.max_stairs = options.get('max_stairs', 1)
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

                cell = self.data['grid'].randomCell(floor)
                if cell.blocked:
                    continue

                if floor > 0:
                    previous_floor_cell = self.data['grid'].cells[floor - 1][cell.y][cell.x]
                    if previous_floor_cell.blocked:
                        previous_floor_cell = None

                next_floor_cell = self.data['grid'].cells[floor + 1][cell.y][cell.x]
                if next_floor_cell is None or next_floor_cell.blocked:
                    continue

                cell.stairs = {
                    'next_floor': next_floor_cell,
                    'direction': 'up' if self.options['ascending'] else 'down'
                }
                if next_floor_cell:
                    next_floor_cell.stairs = {
                        'previous_floor': cell,
                        'direction': 'down' if self.options['ascending'] else 'up'
                    }
                total_stairs_by_floor[floor] = total_stairs_by_floor.get(floor, 0) + 1