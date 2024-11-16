import argparse
from pymazebuilder.generators.dungeon import DungeonGenerator
from pymazebuilder.generators.generator_manager import GeneratorManager
from pymazebuilder.generators.maze import MazeGenerator
from pymazebuilder.renderer import Renderer
from pymazebuilder.generators.room import RoomGenerator
from pymazebuilder.generators.stairs import StairsGenerator
from pymazebuilder.utils import Random

SEED = 100

def main():
    parser = argparse.ArgumentParser(description='Generate a maze or a dungeon.')
    parser.add_argument('--type', type=str, default='maze', help='Type of maze to generate (dungeon or maze)')
    parser.add_argument('--width', type=int, default=21, help='Width of the grid')
    parser.add_argument('--height', type=int, default=21, help='Height of the grid')
    parser.add_argument('--floors', type=int, default=2, help='Number of floors')
    parser.add_argument('--min_rooms', type=int, default=1, help='Minimum number of rooms')
    parser.add_argument('--max_rooms', type=int, default=8, help='Maximum number of rooms')
    parser.add_argument('--min_room_width', type=int, default=1, help='Minimum room width')
    parser.add_argument('--min_room_height', type=int, default=1, help='Minimum room height')
    parser.add_argument('--max_room_width', type=int, default=8, help='Maximum room width')
    parser.add_argument('--max_room_height', type=int, default=8, help='Maximum room height')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed for random number generator')
    args = parser.parse_args()

    Random.seed(args.seed)

    if args.type == "dungeon":
        Renderer(GeneratorManager([
            {
                'generator': DungeonGenerator,
                'options': {
                    'width': args.width,
                    'height': args.height,
                    'floors': args.floors,
                    'min_rooms': args.min_rooms,
                    'max_rooms': args.max_rooms,
                    "min_room_width": args.min_room_width,
                    "min_room_height": args.min_room_height,
                    "max_room_width": args.max_room_width,
                    "max_room_height": args.max_room_height
                }
            },
            {
                'generator': StairsGenerator,
                'options': {}
            }
        ]))
    else:
        Renderer(GeneratorManager([
            {
                'generator': MazeGenerator,
                'options': {
                    'width': args.width,
                    'height': args.height,
                    'floors': args.floors
                }
            },
            {
                'generator': StairsGenerator,
                'options': {}
            }
        ]))

if __name__ == '__main__':
    main()
