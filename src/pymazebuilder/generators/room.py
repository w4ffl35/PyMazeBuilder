from pymazebuilder.utils import Random


class RoomGenerator:
    def __init__(
        self,
        data=None,
        min_rooms=1,
        max_rooms=8,
        min_room_width=1,
        min_room_height=1,
        max_room_width=8,
        max_room_height=8,
        total_rooms=None
    ):
        self.data = data or {}
        self.data['rooms'] = []
        self.min_rooms = min_rooms
        self.max_rooms = max_rooms
        self.min_room_width = min_room_width
        self.min_room_height = min_room_height
        self.max_room_width = max_room_width
        self.max_room_height = max_room_height
        self.totalRooms = total_rooms or Random.range(self.min_rooms, self.max_rooms)
        self.generate()

    def generate(self):
        for z in range(self.data['grid'].total_floors):
            for i in range(self.totalRooms):
                room_width = Random.range(self.min_room_width, self.max_room_width)
                room_height = Random.range(self.min_room_height, self.max_room_height)
                room = {
                    'x': Random.range(0, self.data['grid'].width - room_width),
                    'y': Random.range(0, self.data['grid'].height - room_height),
                    'width': room_width,
                    'height': room_height
                }
                for y in range(room['y'], room['y'] + room['height']):
                    for x in range(room['x'], room['x'] + room['width']):
                        if self.data['grid'].isInNavigationBounds(x, y):
                            self.data['grid'].unblockCell(x, y, z)
                self.data['rooms'].append(room)
