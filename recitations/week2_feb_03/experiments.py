from math165 import *


class Problem1(Counter):
    def __init__(self):
        super().__init__()
        self.dice = Dice()

    def sample(self) -> Any:
        return tuple(self.dice.roll() for _ in range(3))

    def judge(self, result: Any) -> bool:
        x, y, z = result
        if x == y or x == z or y == z:
            return True
        return False


class Problem2(Counter):
    def sample(self) -> Any:
        hand = Deck().shuffle().deal(5)
        return hand

    def judge(self, result: Any) -> bool:
        suits = [card.suit for card in result]
        if len(set(suits)) < 4:
            return True
        return False


class Problem3(Counter):
    def sample(self) -> Any:
        hand = Deck().shuffle().deal(3)
        return hand

    def condition(self, result: Any) -> bool:
        if result[0] != Spades(Rank.Ace):
            return False
        if result[1] != Clubs(Rank.Eight):
            return False
        return True

    def judge(self, result: Any) -> bool:
        return result[2].rank == Rank.Ace


class Problem3Conditional(Problem3):
    def __init__(self):
        super().__init__()
        self.deck = Deck()
        self.deck.remove(Rank.Ace.of(Suit.Spades))
        self.deck.remove(Rank.Eight.of(Suit.Clubs))

    def sample(self) -> Any:
        return self.deck.roll()

    def condition(self, result: Any) -> bool:
        return True

    def judge(self, result: Any) -> bool:
        return result.rank == Rank.Ace


print(Problem1().do_many(10_000))
print(Problem2().do_many(10_000))
print(Problem3().do_many(10_000))
print(Problem3Conditional().do_many(10_000))
