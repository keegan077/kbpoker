from typing import Union, List, NoReturn
from cards import Card
import random


class Deck:

    def __init__(self):
        self._cards_undealt: List[Card] = []
        self._cards_dealt:   List[Card] = []

        for suit in Card.SUITS:
            for rank in Card.RANK.keys():
                self._cards_undealt.append(Card(rank, suit))

    def shuffle(self) -> NoReturn:
        """
        Shuffles the remaining cards in the deck.
        Cards that have already been dealt are not affected
        """
        random.shuffle(self._cards_undealt)

    def deal(self, count: int = 1) -> Union[Card, List[Card]]:
        """
        Deals a number of cards, and puts them in a pile of dealt cards
        Returns a single card if count is 1, otherwise a list of cards
        """
        try:
            for i in range(count):
                self._cards_dealt.append(self._cards_undealt.pop())
        except IndexError:
            raise Deck.DealException("not enough cards in deck")

        if count == 1:
            return self._cards_dealt[-1]
        return self._cards_dealt[-count:-1]

    def reset(self) -> NoReturn:
        """
        Puts all dealt cards back on the undealt deck pile.
        No shuffle is performed, this should be called separately
        """
        for i in self._cards_dealt:
            self._cards_undealt.append(self._cards_dealt.pop())

    def __len__(self):
        return len(self._cards_undealt)

    class DealException(BaseException):
        pass
