from utils import Random

class RoomGenerator:
    def __init__(self, data, options):
        self.options = options
        self.data = data or {}
        self.data['rooms'] = []
        minRooms = int(options.get('minRooms', 1))
        maxRooms = int(options.get('maxRooms', 8))
        self.minRoomWidth = int(options.get('minRoomWidth', 1))
        self.minRoomHeight = int(options.get('minRoomHeight', 1))
        self.maxRoomWidth = int(options.get('maxRoomWidth', 8))
        self.maxRoomHeight = int(options.get('maxRoomHeight', 8))
        self.totalRooms = options.get('totalRooms', Random.range(minRooms, maxRooms))
        self.generate()

    def generate(self):
        for z in range(self.data['grid'].total_floors):
            for i in range(self.totalRooms):
                roomWidth = Random.range(self.minRoomWidth, self.maxRoomWidth)
                roomHeight = Random.range(self.minRoomHeight, self.maxRoomHeight)
                room = {
                    'x': Random.range(0, self.data['grid'].width - roomWidth),
                    'y': Random.range(0, self.data['grid'].height - roomHeight),
                    'width': roomWidth,
                    'height': roomHeight
                }
                for y in range(room['y'], room['y'] + room['height']):
                    for x in range(room['x'], room['x'] + room['width']):
                        if self.data['grid'].isInNavigationBounds(x, y):
                            self.data['grid'].unblockCell(x, y, z)
                self.data['rooms'].append(room)