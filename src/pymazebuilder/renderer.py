from typing import Any

from pymazebuilder.generators.generator_manager import GeneratorManager

class Renderer:
    def __init__(self, generator: GeneratorManager):
        self.generator: GeneratorManager = generator
        self.do_render(generator)

    def do_render(self, generator: GeneratorManager = None):
        for row in self.render(generator):
            print(row)

    def render(self, generator):
        for y in range(generator.data['grid'].height):
            row = ''
            for x in range(generator.data['grid'].width):
                cell = generator.data['grid'].cells[y][x]
                row = self.draw_cell(row=row, cell=cell)
            yield row

    def draw_cell(self, **kwargs) -> Any:
        row = kwargs.get('row')
        cell = kwargs.get('cell')
        f = '\u2588' if cell.blocked else '\u2591'
        if cell.stairs:
            if cell.stairs['direction'] == 'up':
                f = '\u25B2'
            else:
                f = '\u25BC'
        row += f
        return row
