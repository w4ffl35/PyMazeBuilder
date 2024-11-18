import argparse

from pymazebuilder.ascii_renderer import ASCIIRenderer
from pymazebuilder.generators.dungeon import DungeonGenerator
from pymazebuilder.generators.generator_manager import GeneratorManager
from pymazebuilder.generators.maze import MazeGenerator
from pymazebuilder.generators.room import RoomGenerator
from pymazebuilder.generators.stairs import StairsGenerator

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
    parser.add_argument('--max_stairs', type=int, default=1, help='Max stairs')
    parser.add_argument('--seed', type=int, default=SEED, help='Seed for random number generator')
    parser.add_argument('--ascending', type=bool, default=False, help='Ascending or descending dungeon / maze')
    parser.add_argument('--current_floor', type=int, default=0, help='Current floor')
    args = parser.parse_args()

    if args.type == "dungeon":
        ASCIIRenderer(GeneratorManager(seed=args.seed, current_floor=args.current_floor, generators=[
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
                'options': {
                    'ascending': args.ascending,
                    'max_stairs': args.max_stairs,
                    'floors': args.floors,
                }
            }
        ]))
    else:
        ASCIIRenderer(GeneratorManager(seed=args.seed, current_floor=args.current_floor, generators=[
            {
                'generator': MazeGenerator,
                'options': {
                    'width': args.width,
                    'height': args.height,
                    'floors': args.floors
                }
            },
            {
                'generator': RoomGenerator,
                'options': {
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
                'options': {
                    'ascending': args.ascending,
                    'max_stairs': args.max_stairs,
                    'floors': args.floors,
                }
            }
        ]))

if __name__ == '__main__':
    main()
