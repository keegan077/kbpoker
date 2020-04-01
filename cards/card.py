from __future__ import annotations


class Card:

    SUITS = ("clubs", "diamonds", "hearts", "spades")
    RANK = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, rank: int, suit: str):
        # TODO: consider Jokers

        if rank < 1 or rank > 13:
            raise Card.RankException("invalid card rank")
        elif suit not in Card.SUITS:
            raise Card.SuitException("invalid card suit")

        self._rank = rank
        self._suit = suit

    def __str__(self):
        return self.rank() + " of " + self.suit()

    def rank(self) -> str:
        return Card.RANK[self._rank]

    def suit(self) -> str:
        return self._suit.capitalize()

    def __eq__(self, other: Card):
        if not type(other) is Card:
            return False
        return self.suit() == other.suit() and self.rank() == other.rank()

    class RankException(Exception):
        pass

    class SuitException(Exception):
        pass
