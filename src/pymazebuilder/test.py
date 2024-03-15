from pymazebuilder.generators.generator import Generator
from pymazebuilder.generators.maze import MazeGenerator
from pymazebuilder.renderer import Renderer
from pymazebuilder.generators.room import RoomGenerator
from pymazebuilder.generators.stairs import StairsGenerator
from pymazebuilder.utils import Random

SEED = 100
WIDTH = 21
HEIGHT = 21
FLOORS = 2
MIN_ROOMS = 1
MAX_ROOMS = 8
MIN_ROOM_WIDTH = 1
MIN_ROOM_HEIGHT = 1
MAX_ROOM_WIDTH = 8
MAX_ROOM_HEIGHT = 8

Random.seed(SEED)

generator = Generator([
    {
        'generator': MazeGenerator,
        'options': {
            'width': WIDTH,
            'height': HEIGHT,
            'floors': FLOORS
        }
    },
    {
        'generator': RoomGenerator,
        'options': {
            'minRooms': MIN_ROOMS,
            'maxRooms': MAX_ROOMS,
            'minRoomWidth': MIN_ROOM_WIDTH,
            'minRoomHeight': MIN_ROOM_HEIGHT,
            'maxRoomWidth': MAX_ROOM_WIDTH,
            'maxRoomHeight': MAX_ROOM_HEIGHT
        }
    },
    {
        'generator': StairsGenerator,
        'options': {}
    }
])


parsed_data = generator.to_json()
print(parsed_data)