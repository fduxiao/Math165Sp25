from .sampler import Sampler


class Dice(Sampler):
    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)
