from grid import Grid
from utils import Random


class MazeGenerator:
    def __init__(self, data, options):
        self.data = data or {}
        self.options = options
        self.neighbor_positions = options.get('neighbor_positions', [[0, -2], [0, 2], [-2, 0], [2, 0]])
        self.start_cell_coord = {'x': 1, 'y': 1}
        GridClass = options.get('grid_class', Grid)
        self.data['grid'] = GridClass({
            'width': options.get('width'),
            'height': options.get('height'),
            'total_floors': options.get('floors'),
            'cell_class': options.get('cell_class'),
            'start_x': options.get('start_x'),
            'start_y': options.get('start_y'),
            'start_z': options.get('start_z'),
            'floors': []
        })
        self.generate()

    def getNeighborCells(self, cell):
        neighbor_cells = []
        for i in range(4):
            nx = cell.x + self.neighbor_positions[i][0]
            ny = cell.y + self.neighbor_positions[i][1]
            neighbor_cell = self.data['grid'].getNeighborCell(nx, ny, cell.z)
            if neighbor_cell and not neighbor_cell.visited and neighbor_cell.blocked:
                neighbor_cells.append(neighbor_cell)
        return neighbor_cells

    def generate(self):
        for z in range(self.data['grid'].total_floors):
            x = self.start_cell_coord['x']
            y = self.start_cell_coord['y']
            get_cell = True
            prev_cells = []
            current_cell = self.data['grid'].getCell(x, y, z)

            while get_cell:
                current_cell.visited = True
                neighbor_cells = self.getNeighborCells(current_cell)
                if len(neighbor_cells) > 0:
                    neighbor_cell = neighbor_cells[Random.range(0, len(neighbor_cells))]
                    n_x = current_cell.x
                    n_y = current_cell.y
                    if neighbor_cell.x > current_cell.x:
                        n_x += 1
                    elif neighbor_cell.x < current_cell.x:
                        n_x -= 1
                    if neighbor_cell.y > current_cell.y:
                        n_y += 1
                    elif neighbor_cell.y < current_cell.y:
                        n_y -= 1
                    new_cell = self.data['grid'].getCell(n_x, n_y, z)
                    new_cell.blocked = False
                    current_cell.blocked = False
                    prev_cells.append(current_cell)
                    current_cell = neighbor_cell
                else:
                    if len(prev_cells) > 0:
                        current_cell = prev_cells.pop()
                    else:
                        get_cell = False