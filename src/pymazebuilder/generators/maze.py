from pymazebuilder.grid import Grid
from pymazebuilder.utils import Random


class MazeGenerator:
    def __init__(
        self,
        data=None,
        neighbor_positions=None,
        grid_class=Grid,
        width=None,
        height=None,
        floors=None,
        cell_class=None,
        start_x=None,
        start_y=None,
        start_z=None,
        min_rooms=None,
        max_rooms=None,
    ):
        self.data = data or {}
        self.neighbor_positions = neighbor_positions or [[0, -2], [0, 2], [-2, 0], [2, 0]]
        self.start_cell_coord = {'x': 1, 'y': 1}
        GridClass = grid_class
        self.data['grid'] = GridClass({
            'width': width,
            'height': height,
            'total_floors': floors,
            'cell_class': cell_class,
            'start_x': start_x,
            'start_y': start_y,
            'start_z': start_z,
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