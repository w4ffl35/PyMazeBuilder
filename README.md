# PyMazeBuilder

Generate perfect mazes with Python using a growing tree algorithm.

---

## Installation

```bash
pip install pymazebuilder
```

---

```bash
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
```

Generated data structure

```python
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
```

---

## Quick use

### Example

Generate a maze

```bash
python main.py
```

Generate a dungeon

```bash
python main.py --type=dungeon
```

The built-in renderer is a simple ASCII renderer which prints the maze to the console.

```python
from pymazebuilder.generators.generator import Generator
from pymazebuilder.generators.maze import MazeGenerator
from pymazebuilder.renderer import Renderer
data = Generator([
    {
        'generator': MazeGenerator,
        'options': {
            'width': 10,
            'height': 10,
            'floors': 1
        }
    },
])
Renderer(data)
```

---

## Randomization

`utils.py` contains a random class which handles all random number generation and can be seeded.

---

### Generator classes

Generator classes can be passed as an optional array of objects to the maze generator.

The shape of this data structure is as follows:

```python
[
    {
        generator: <generator class>,
        options: <options object>
    },
    ...
]
```

`Generator` (`src/pymaze/generator.py`) will iterate over each generator class and instantiate it.

**Example**

The following example shows how to generate a maze with rooms using the provided room generator.

(also see `src/pymaze/main.py`)

```python
from pymazebuilder.generators.generator import Generator
from pymazebuilder.generators.renderer import Renderer

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
```

#### Multi-floor maze

Use the `floors` option to generate a multi-floor maze.

Use the `src/generators/stairs.py` generator to connect the floors with stairs.

```bash
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
```

---

Dungeon

```bash
█████████████████████
█████████████████████
█░░░░░░░░░░░░░░░░████
█░░░░██████████░░████
█░░░░█░░░░░░░░░░░████
█░░░░░░░░░░░░░█░░████
██░██████████░█░░████
██░██████████░█░░████
██░█████████░░░░░████
██░█████░░░░░░░██████
██░░░░░░░░██░░░██████
██░░██░░░░███████████
█░░░░░░░░░███████████
█░░░░░░░░░███████████
█░░░░░░░░░███████████
█░░░░░███████████████
█░░░░░███████████████
█░░░░░███████████████
█░░░░░███████████████
█████████████████████
█████████████████████
```

---

#### Custom generator classes

Custom generators should match the following pattern.

```python
class SomeGenerator:
    def __init__(data: dict, options: dict):
        # do something with the data object
        self.data = data
        self.data["some_property"] = "some value"
```

See `src/pymaze/room.py` and `src/pymaze/maze.py` for complete examples along with a list of optional arguments that each class takes.
    
---

## License

[GNU GPL 3](LICENSE)

---

## Contributors

  - [@w4ffl35](https://github.com/w4ffl35)
