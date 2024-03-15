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

Renderer(Generator([
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
            'min_rooms': MIN_ROOMS,
            'max_rooms': MAX_ROOMS,
            'min_room_width': MIN_ROOM_WIDTH,
            'min_room_height': MIN_ROOM_HEIGHT,
            'max_room_width': MAX_ROOM_WIDTH,
            'max_room_height': MAX_ROOM_HEIGHT
        }
    },
    {
        'generator': StairsGenerator,
        'options': {}
    }
]))