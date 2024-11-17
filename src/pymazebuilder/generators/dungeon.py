from typing import Optional

from pymazebuilder.generators.generator import Generator
from pymazebuilder.grid import Grid
from pymazebuilder.utils import Random


class DungeonGenerator(Generator):
    def __init__(
        self,
        data: Optional[dict] = None,
        grid_class: type = Grid,
        width: Optional[int] = None,
        height: Optional[int] = None,
        floors: Optional[int] = None,
        cell_class=None,
        start_x: Optional[int] = None,
        start_y: Optional[int] = None,
        start_z: Optional[int] = None,
        min_rooms: int = 6,
        max_rooms: int = 12,
        min_room_width: int = 6,
        min_room_height: int = 6,
        max_room_width: int = 12,
        max_room_height: int = 12,
        current_floor: int = 0,
        previous_floor_data: Optional[dict] = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.rooms = None
        self.data = data or {}
        self.start_cell_coord = {'x': start_x or 1, 'y': start_y or 1}
        self.grid_class = grid_class
        self.width = width
        self.height = height
        self.floors = floors
        self.cell_class = cell_class
        self.min_rooms = min_rooms
        self.max_rooms = max_rooms
        self.min_room_width = min_room_width
        self.max_room_width = max_room_width
        self.min_room_height = min_room_height
        self.max_room_height = max_room_height
        self.current_floor = current_floor
        self.previous_floor_data = previous_floor_data
        self.data['grid'] = self.grid_class(
            width=self.width,
            height=self.height,
            cell_class=self.cell_class,
            start_x=self.start_cell_coord['x'],
            start_y=self.start_cell_coord['y'],
            start_z=self.current_floor
        )
        self.generate_floor(self.current_floor)

    def generate_floor(self, floor):
        self.rooms = []  # Reset rooms for the new floor
        self._create_rooms(floor)
        self._connect_rooms(floor)

    def _create_rooms(self, floor):
        num_rooms = Random.range(self.min_rooms, self.max_rooms)
        for _ in range(num_rooms):
            room_width = Random.range(self.min_room_width, self.max_room_width)
            room_height = Random.range(self.min_room_height, self.max_room_height)
            room_x = Random.range(0, self.data['grid'].width - room_width)
            room_y = Random.range(0, self.data['grid'].height - room_height)
            self._create_room(room_x, room_y, room_width, room_height, floor)

    def _create_room(self, x, y, width, height, floor):
        room_cells = []
        for i in range(width):
            for j in range(height):
                cell = self.data['grid'].get_cell(x + i, y + j, floor)
                cell.blocked = False
                room_cells.append(cell)
        self.rooms.append(room_cells)

    def _connect_rooms(self, floor):
        for i in range(len(self.rooms) - 1):
            room_a = self.rooms[i]
            room_b = self.rooms[i + 1]
            center_a = room_a[len(room_a) // 2]
            center_b = room_b[len(room_b) // 2]
            self._create_corridor(center_a, center_b, floor)

    def _create_corridor(self, start, end, floor):
        current_x, current_y = start.x, start.y
        while current_x != end.x or current_y != end.y:
            if current_x != end.x:
                current_x += 1 if end.x > current_x else -1
            elif current_y != end.y:
                current_y += 1 if end.y > current_y else -1
            cell = self.data['grid'].get_cell(current_x, current_y, floor)
            cell.blocked = False
