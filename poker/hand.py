from __future__ import annotations
from typing import List
from cards import Card


class Hand:
    """
    A class to represent a theoretical hand based on a number of input cards
    """

    # Hands and their corresponding rankings, higher is better
    # https://www.cardschat.com/poker-hands/
    HANDS = {
        "royal_flush":      10,
        "straight_flush":   9,
        "four_of_a_kind":   8,
        "full_house":       7,
        "flush":            6,
        "straight":         5,
        "three_of_a_kind":  4,
        "two_pair":         3,
        "one_pair":         2,
        "high_card":        1,
    }

    def __init__(self, *cards: Card):
        self._cards: List[Card] = [card for card in cards]

    def best_hand(self) -> str:
        """
        Returns the string name of the best possible hand from the combination of cards given
        :return:
        """

    def __len__(self):
        return len(self._cards)

    def __eq__(self, other: Hand):
        pass
