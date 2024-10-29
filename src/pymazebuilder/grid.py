from pymazebuilder.cell import Cell
from pymazebuilder.utils import Random

MIN_WIDTH = 5
MIN_HEIGHT = 5
MIN_BOUNDARY = -1
MIN_NEIGHBOR_BOUNDARY = 0
MIN_FLOORS = 1


class Grid:
    def __init__(self, options):
        self.width = int(options.get('width') or MIN_WIDTH)
        self.height = int(options.get('height') or MIN_HEIGHT)
        self.total_floors = int(options.get('total_floors') or MIN_FLOORS)
        self.start_x = int(options.get('start_x') or 0)
        self.start_y = int(options.get('start_y') or 0)
        self.start_z = int(options.get('start_z') or 0)
        self.CellClass = options.get('cell_class') or Cell
        self.currentFloor = options.get('currentFloor', 0)
        if self.width <= MIN_WIDTH: self.width = MIN_WIDTH
        if self.height <= MIN_HEIGHT: self.height = MIN_HEIGHT
        if self.start_x > self.width - 1: self.start_x = self.start_x - 1
        if self.start_y > self.height - 1: self.start_y = self.start_y - 1
        if self.start_z >= self.total_floors: self.start_z = self.total_floors - 1
        self.floors = []
        self.cells = options.get("cells", None)
        if not self.cells:
            self.initialize()
    
    def to_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'total_floors': self.total_floors,
            'start_x': self.start_x,
            'start_y': self.start_y,
            'start_z': self.start_z,
            'currentFloor': self.currentFloor,
            'floors': self.floors,
            'cells': [[[cell.to_dict() for cell in row] for row in floor] for floor in self.cells]
        }

    @classmethod
    def from_dict(cls, data: dict):
        grid = cls({
            'width': data['width'],
            'height': data['height'],
            'total_floors': data['total_floors'],
            'start_x': data['start_x'],
            'start_y': data['start_y'],
            'start_z': data['start_z'],
            'currentFloor': data['currentFloor'],
            'floors': data['floors'],
            'cells': data['cells'],
            'cell_class': data['cell_class']
        })
        grid.cells = [[[data['cell_class'].from_dict(cell) for cell in row] for row in floor] for floor in data['cells']]
        return grid

    def initialize(self):
        self.cells = []
        for z in range(self.start_z, self.total_floors):
            self.floors.append({})  # set floor data to an empty object
            self.cells.append([])
            for y in range(self.start_y, self.height):
                self.cells[z].append([])
                for x in range(self.start_x, self.width):
                    self.cells[z][y].append(self.CellClass(x, y, z))

    def random_cell(self, z):
        x = Random.range(MIN_NEIGHBOR_BOUNDARY, self.width - 2)
        y = Random.range(MIN_NEIGHBOR_BOUNDARY, self.height - 2)
        return self.get_cell(x, y, z)

    def is_in_bounds(self, x, y):
        return x < self.width and x > MIN_BOUNDARY and y < self.height and y > MIN_BOUNDARY

    def is_in_navigation_bounds(self, x, y):
        return x < self.width - 1 and x > MIN_NEIGHBOR_BOUNDARY and y < self.height - 1 and y > MIN_NEIGHBOR_BOUNDARY

    def get_cell(self, x, y, z) -> Cell:
        cell = self.cells[z][y][x] if self.is_in_bounds(x, y) else None
        if cell == []:
            return None
        return cell

    def get_neighbor_cell(self, x, y, z):
        return self.cells[z][y][x] if self.is_in_navigation_bounds(x, y) else None

    def unblock_cell(self, x, y, z):
        if self.is_in_bounds(x, y):
            self.cells[z][y][x].blocked = False
