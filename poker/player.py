from __future__ import annotations
from enum import Enum
from typing import List, Tuple, Optional
from cards import Card


class Player:
    """
    Represents a Player in a poker game.
    """

    def __init__(self, player_name: str = None, player_id: str = None):
        assert player_name is not None
        assert player_id is not None

        self.name:  str = player_name
        self.id:    str = player_id

        self._chips:        int = 0
        self._pocket_cards: List[Card, Card] = []

    def clear_pocket_cards(self):
        self._pocket_cards.clear()

    def set_pocket_cards(self, cards: List[Card]):
        assert len(cards) == 2, "player can only be given 2 pocket cards"
        self._pocket_cards.clear()
        self._pocket_cards.extend(cards)


class PlayerAction:

    class ActionType:
        CHECKFOLD = 1
        FOLD = 2
        CHECK = 3
        SEE = 4
        RAISE = 5

    def __init__(self):
        self.action: PlayerAction.ActionType = PlayerAction.ActionType.CHECKFOLD
        self.value: int = 0
