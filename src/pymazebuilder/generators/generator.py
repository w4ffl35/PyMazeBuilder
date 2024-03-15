import json


class Generator:
    def __init__(self, generators):
        self.data = {}
        self.generators = []
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
        data = self.data
        data["grid"] = data["grid"].to_dict()
        return json.dumps(data, indent=4)