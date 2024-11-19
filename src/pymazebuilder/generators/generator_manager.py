import json
from typing import List, Optional

from pymazebuilder.cell import Cell
from pymazebuilder.grid import Grid
from pymazebuilder.utils import Random


class GeneratorManager:
    def __init__(self, seed: int = 42, current_floor: int = 0, generators: Optional[List[dict]] = None):
        self._seed = None
        self.current_floor = current_floor
        self.seed = seed + current_floor
        self.data = {}
        self.generators = []
        generators = [] if not generators else generators
        for generator in generators:
            generator_instance = generator['generator'](
                data=self.data,
                current_floor=self.current_floor,
                seed=self.seed,
                **generator['options']
            )
            self.generators.append(generator_instance)
            self.data = generator_instance.data

        if self.current_floor > 0:
            self.previous_floor_data = self._generate_previous_floor(seed, current_floor - 1, generators)
        else:
            self.previous_floor_data = None

    def _generate_previous_floor(self, seed, floor, generators):
        previous_data = {}
        for generator in generators:
            generator_instance = generator['generator'](
                data=previous_data,
                current_floor=floor,
                **generator['options']
            )
            generator_instance.generate()
            previous_data = generator_instance.data
        return previous_data

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, value):
        self._seed = value
        Random.seed(value)

    def to_json(self):
        data = self.data.copy()
        data["grid"] = data["grid"].to_dict()
        return json.dumps(data, indent=4)

    def from_dict(self, data: dict):
        cells = []
        cell_class = data["grid"]["cell_class"]
        for row in data["grid"]["cells"]:
            cells.append([cell_class.from_dict(cell) for cell in row])

        data["grid"] = Grid(
            width=data["grid"]["width"],
            height=data["grid"]["height"],
            cell_class=data["grid"]["cell_class"],
            start_x=data["grid"]["start_x"],
            start_y=data["grid"]["start_y"],
            start_z=data["grid"]["start_z"],
            cells=cells
        )
        self.data = data
