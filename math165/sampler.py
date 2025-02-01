import random
from typing import Any


class Sampler(list):
    def __init__(self, *args):
        super().__init__(args)

    def shuffle(self):
        random.shuffle(self)

    def deal(self, n: int):
        result = []
        for _ in range(n):
            result.append(self.pop(0))
        return result

    def roll(self):
        self.shuffle()
        return self[0]


class Counter:
    def __init__(self):
        self.count = 0
        self.hit = 0

    def sample(self) -> Any:
        pass

    def judge(self, result: Any) -> bool:
        pass

    def do(self):
        result = self.sample()
        if self.judge(result):
            self.hit += 1
        self.count += 1
        return result

    def do_many(self, n):
        for _ in range(n):
            self.do()
        return self

    def __repr__(self):
        pass
