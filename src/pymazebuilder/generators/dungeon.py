from typing import Optional

from pymazebuilder.generators.generator import Generator
from pymazebuilder.grid import Grid
from pymazebuilder.utils import Random


class DungeonGenerator(Generator):
    def __init__(
        self,
        data:Optional[dict]=None,
        grid_class:type=Grid,
        width:Optional[int]=None,
        height:Optional[int]=None,
        floors:Optional[int]=None,
        cell_class=None,
        start_x:Optional[int]=None,
        start_y:Optional[int]=None,
        start_z:Optional[int]=None,
        min_rooms:int=6,
        max_rooms:int=12,
        min_room_width:int=6,
        min_room_height:int=6,
        max_room_width:int=12,
        max_room_height:int=12,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.data = data or {}
        self.start_cell_coord = {'x': start_x or 1, 'y': start_y or 1}
        self.data['grid'] = grid_class(
            width=width,
            height=height,
            total_floors=floors,
            cell_class=cell_class,
            start_x=start_x,
            start_y=start_y,
            start_z=start_z
        )
        self.min_rooms = min_rooms
        self.max_rooms = max_rooms
        self.min_room_width = min_room_width
        self.max_room_width = max_room_width
        self.min_room_height = min_room_height
        self.max_room_height = max_room_height
        self.rooms = []
        self.generate()

    def generate(self):
        for z in range(self.data['grid'].total_floors):
            self._create_rooms(z)
            self._connect_rooms(z)

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
        current = start
        while current.x != end.x or current.y != end.y:
            if current.x != end.x:
                current.x += 1 if end.x > current.x else -1
            elif current.y != end.y:
                current.y += 1 if end.y > current.y else -1
            cell = self.data['grid'].get_cell(current.x, current.y, floor)
            cell.blocked = False
