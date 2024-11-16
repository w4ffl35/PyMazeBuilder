import json
from typing import List, Optional

from pymazebuilder.cell import Cell
from pymazebuilder.grid import Grid


class GeneratorManager:
    def __init__(self, generators: Optional[List[dict]]=None):
        self.data = {}
        self.generators = []
        generators = [] if not generators else generators
        for generator in generators:
            generator_instance = generator['generator'](
                data=self.data,
                **generator['options']
            )
            self.generators.append(generator_instance)
            self.data = generator_instance.data

    def generate(self):
        for generator in self.generators:
            generator.generate()

    def to_json(self):
        data = self.data.copy()
        data["grid"] = data["grid"].to_dict()
        return json.dumps(data, indent=4)

    def from_dict(self, data: dict):
        cells = []
        for floor in data["grid"]["cells"]:
            floor_cells = []
            for row in floor:
                floor_cells.append([Cell.from_dict(cell) for cell in row])
            cells.append(floor_cells)

        data["grid"] = Grid(
            width=data["grid"]["width"],
            height=data["grid"]["height"],
            total_floors=data["grid"]["total_floors"],
            cell_class=Cell,
            start_x=data["grid"]["start_x"],
            start_y=data["grid"]["start_y"],
            start_z=data["grid"]["start_z"],
            floors=data["grid"]["floors"],
            cells=cells
        )
        self.data = data
