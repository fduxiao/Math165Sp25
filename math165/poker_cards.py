from dataclasses import dataclass
from enum import Enum, auto

from .sampler import Sampler


class Suit(Enum):
    Clubs = auto()
    Diamonds = auto()
    Hearts = auto()
    Spades = auto()


class Rank(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 0
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

    def of(self, suit: Suit):
        return Card(self).of(suit)


@dataclass(order=True)
class Card:
    rank: Rank
    suit: Suit = None

    def of(self, suit: Suit):
        return Card(self.rank, suit)


class SuitMaker:
    suit: Suit = None

    def __new__(cls, rank):
        return Card(rank, cls.suit)


class Clubs(SuitMaker):
    suit = Suit.Clubs


class Diamonds(SuitMaker):
    suit = Suit.Diamonds


class Hearts(SuitMaker):
    suit = Suit.Hearts


class Spades(SuitMaker):
    suit = Suit.Spades


class Deck(Sampler):
    default_deck = [Card(rank).of(suit) for suit in Suit for rank in Rank]
    def __init__(self):
        super().__init__(*self.default_deck)
