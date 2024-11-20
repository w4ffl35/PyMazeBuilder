from typing import Any, Optional

from pymazebuilder.cell import Cell
from pymazebuilder.utils import Random

MIN_WIDTH = 5
MIN_HEIGHT = 5
MIN_BOUNDARY = -1
MIN_NEIGHBOR_BOUNDARY = 0
MIN_FLOORS = 1


class Grid:
    def __init__(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        start_x: Optional[int] = None,
        start_y: Optional[int] = None,
        start_z: Optional[int] = None,
        cell_class=None,
        cells: Optional[list] = None
    ):
        self.width = width or MIN_WIDTH
        self.height = height or MIN_HEIGHT
        self.start_x = start_x or 0
        self.start_y = start_y or 0
        self.start_z = start_z or 0
        self.CellClass = cell_class or Cell
        if self.width <= MIN_WIDTH: self.width = MIN_WIDTH
        if self.height <= MIN_HEIGHT: self.height = MIN_HEIGHT
        if self.start_x > self.width - 1: self.start_x = self.start_x - 1
        if self.start_y > self.height - 1: self.start_y = self.start_y - 1
        self.cells = cells
        if not self.cells:
            self.initialize()

    def to_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'start_x': self.start_x,
            'start_y': self.start_y,
            'start_z': self.start_z,
            'cells': [[cell.to_dict() for cell in row] for row in self.cells],
            'cell_class': self.CellClass
        }

    @classmethod
    def from_dict(cls, data: dict):
        grid = cls(
            width=data['width'],
            height=data['height'],
            start_x=data['start_x'],
            start_y=data['start_y'],
            start_z=data['start_z'],
            cell_class=data['cell_class']
        )
        grid.cells = [[data['cell_class'].from_dict(cell) for cell in row] for row in data['cells']]
        return grid

    def initialize(self):
        self.cells = []
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                cell = self.CellClass(x, y, self.start_z)
                self.cells[y].append(cell)

    def random_cell(self):
        x = Random.range(MIN_NEIGHBOR_BOUNDARY, self.width - 2)
        y = Random.range(MIN_NEIGHBOR_BOUNDARY, self.height - 2)
        return self.get_cell(x, y, self.start_z)

    def is_in_bounds(self, x, y):
        return x < self.width and x > MIN_BOUNDARY and y < self.height and y > MIN_BOUNDARY

    def is_in_navigation_bounds(self, x, y):
        return x < self.width - 1 and x > MIN_NEIGHBOR_BOUNDARY and y < self.height - 1 and y > MIN_NEIGHBOR_BOUNDARY

    def get_cell(self, x, y, z) -> Cell:
        cell = self.cells[y][x] if self.is_in_bounds(x, y) else None
        if cell == []:
            return None
        return cell

    def get_neighbor_cell(self, x, y, z):
        return self.cells[y][x] if self.is_in_navigation_bounds(x, y) else None

    def unblock_cell(self, x, y, z):
        if self.is_in_bounds(x, y):
            self.cells[y][x].blocked = False

    def get_neighbors(self, cell):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = cell.x + i
                y = cell.y + j
                if self.is_in_bounds(x, y):
                    neighbor = self.get_cell(x, y, cell.z)
                    if neighbor and neighbor != cell:
                        neighbors.append(neighbor)
        return neighbors

    def get_within_radius(self, cell, radius):
        neighbors = []
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                x = cell.x + i
                y = cell.y + j
                if self.is_in_bounds(x, y):
                    neighbor = self.get_cell(x, y, cell.z)
                    if neighbor and neighbor != cell:
                        neighbors.append(neighbor)
        return neighbors

    def get_within_bounds(self, cell, width, height):
        neighbors = []
        for x in range(0, width):
            for y in range(0, height):
                neighbors.append(self.get_cell(cell.x + x, cell.y + y, cell.z))
        return neighbors
