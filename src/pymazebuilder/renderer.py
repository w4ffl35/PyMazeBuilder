from pymazebuilder.generators.generator_manager import GeneratorManager

class Renderer:
    def __init__(self, generator:GeneratorManager):
        self.generator:GeneratorManager = generator
        self.do_render()
    
    def do_render(self, generator:GeneratorManager=None):
        generator = self.generator if not generator else generator
        for z in range(generator.data['grid'].total_floors):
            print(f"Floor {z}")
            for y in range(generator.data['grid'].height):
                row = ''
                for x in range(generator.data['grid'].width):
                    cell = generator.data['grid'].cells[z][y][x]
                    f = '\u2588' if cell.blocked else '\u2591'
                    if cell.stairs:
                        if cell.stairs['direction'] == 'up':
                            f = '\u25B2'
                        else:
                            f = '\u25BC'
                    row += f
                print(row)
