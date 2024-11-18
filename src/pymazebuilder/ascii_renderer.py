from pymazebuilder.renderer import Renderer


class ASCIIRenderer(Renderer):
    def render(self, row=None):
        print(row)
