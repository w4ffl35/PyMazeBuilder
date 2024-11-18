class Generator:
    def __init__(self, *args, **kwargs):
        self.data = kwargs.get("data", {})
        self.current_floor = kwargs.get("current_floor", 0)

    def generate(self) -> dict:
        pass
