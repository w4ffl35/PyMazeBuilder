# PyMazeBuilder

Generate perfect mazes with Node using a growing tree algorithm. This is a python clone of [node-maze-generator](https://github.com/w4ffl35/node-maze-generator).

    █████████████████████
    █░░░░░░░░░█░░░░░░░░██
    ██░░░░░░░░█░█████░███
    █░░░░░░░░░░░█░░██░░░█
    █░░░░░░░░░█░█░█████░█
    █░░░░░░░░░█░░░█░░░█░█
    █░░░░░░░░░█████░█░█░█
    ███░░░░██░░░░░░░█░░░█
    ███░███████████████░█
    █░░░█░░░░░█░░░░░░░░░█
    █░███░███░█░█████████
    █░█░░░███░█░█░░░░░░░█
    █░█░███░█░█░█░█████░█
    █░█░██░░█░█░░░█░░██░█
    █░█░██░░█░█████░███░█
    █░░░█░░░░░░░█░░░░░█░█
    █░███░░░░░░░█░███░█░█
    █░██░░█░░░░░█░█░░░█░█
    █░███░█░█████░█░███░█
    █░░░░░█░░░░░░░█░░░░░█
    █████████████████████
        
Generated data structure

        {
            grid: [
              [
                Cell {
                  x: 0,
                  y: 0,
                  exits: [],
                  blocked: true,
                  displayed: false,
                  visited: false
                },
                ...
              ]
            ]
            rooms: [
                Room {
                    x: 0,
                    y: 0,
                    width: 0,
                    height: 0
                }
            ]
        }

---

## Quick use

    from pymaze.generators.generator import Generator
    from pymaze.generators.maze import MazeGenerator
    from pymaze.renderer import Renderer
    Renderer(Generator([
        {
            'generator': MazeGenerator,
            'options': {
                'width': 10,
                'height': 10,
                'floors': 1
            }
        },
    ]))

---

## Random

`utils.py` contains a random class which handles all random number generation and can be seeded.

---

### Generator classes

Generator classes can be passed as an optional array of objects to the maze generator.

The shape of this data structure is as follows:

        [
            {
                generator: <generator class>,
                options: <options object>
            },
            ...
        ]

`Generator` (`src/pymaze/generator.py`) will iterate over each generator class and instantiate it.

**Example**

The following example shows how to generate a maze with rooms using the provided room generator.

(also see `src/pymaze/main.py`)

    from pymaze.generators.generator import Generator
    Generator([
        {
            'generator': MazeGenerator,
            'options': {
                ...
            }
        },
        {
            'generator': RoomGenerator,
            'options': {
                ...
            }
        },
        {
            'generator': StairsGenerator,
            'options': {
                ...
            }
        }
    ])
    Renderer(generator)

#### Multi-floor maze

Use the `floors` option to generate a multi-floor maze.

Use the `src/generators/stairs.py` generator to connect the floors with stairs.

    Floor 0
    █████████████████████
    █░██░░░░░██░░░░░░░░░█
    █░███░█░███░░░░░█░█░█
    █░░░█░█░░░░░█░░░█░█░█
    ███▼█░█░█████████░█░█
    █░░░█░█░░░█░░░░░█░███
    █░███░███░█░███░█░███
    █░█░░░░██░█░█░░░█░░░█
    █░█░█████░█░█░█░█░░░█
    █░█░░░░░█░███░█░█░░░█
    █░█░░██░█░███░█░█░░░█
    █░█░░░█░█░░░░░█░░░█░█
    █░███░█░███░░░░░█░█░█
    █░██░░█░░░░░░░█░░░█░█
    █░███████████░█░███░█
    █░░░█░░░█░░░█░░░█░░░█
    ███░█░█░█░█░█████░█░█
    ███░░░█░█░█░░░░░░░█░█
    █░█████░█░███░░░░░█░█
    █░░░░░░░░░██░░░░░░░░█
    █████████████████████
    Floor 1
    █████████████████████
    █░░░░░░░░░█░░░░░░░░██
    ██░░░░░░░░█░█████░███
    █░░░░░░░░░░░█░░██░░░█
    █░░▲░░░░░░█░█░█████░█
    █░░░░░░░░░█░░░█░░░█░█
    █░░░░░░░░░█████░█░█░█
    ███░░░░██░░░░░░░█░░░█
    ███░███████████████░█
    █░░░█░░░░░█░░░░░░░░░█
    █░███░███░█░█████████
    █░█░░░███░█░█░░░░░░░█
    █░█░███░█░█░█░█████░█
    █░█░██░░█░█░░░█░░██░█
    █░█░██░░█░█████░███░█
    █░░░█░░░░░░░█░░░░░█░█
    █░███░░░░░░░█░███░█░█
    █░██░░█░░░░░█░█░░░█░█
    █░███░█░█████░█░███░█
    █░░░░░█░░░░░░░█░░░░░█
    █████████████████████

    ▲ = stairs going up
    ▼ = stairs going down
    █ = wall
    ░ = floor


---

#### Custom generator classes

Custom generators should match the following pattern.
    class SomeGenerator:
        def __init__(data: dict, options: dict):
            # do something with the data object
            self.data = data
            self.data["some_property] = "some value"

See `src/pymaze/room.py` and `src/pymaze/maze.py` for complete examples along with a list of optional arguments that each class takes.
    
---

## License

[GNU GPL 3](LICENSE)

---

## Contributors

  - [@w4ffl35](https://github.com/w4ffl35)
