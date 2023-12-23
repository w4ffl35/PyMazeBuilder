import math
import random  # import the random module

class Random:
    _instance = None

    @staticmethod
    def instance():
        if Random._instance is None:
            Random._instance = Random()
        return Random._instance

    def __init__(self, seed=None):
        self._seed = seed or random.random()  # use random.random() instead of math.random()

    @staticmethod
    def seed(seed):
        Random.instance()._seed = seed
        return Random.instance()._seed

    @staticmethod
    def next():
        x = math.sin(Random.instance()._seed) * 10000
        Random.instance()._seed = x - math.floor(x)
        return x - math.floor(x)

    @staticmethod
    def range(min, max):
        return math.floor(Random.next() * (max - min)) + min