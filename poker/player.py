from __future__ import annotations
from typing import List, Tuple, Optional
from poker import PokerGame
from cards import Card


class Player:
    """
    Represents a Player in a poker game.
    """

    def __init__(self, player_name: str = "", poker_game: PokerGame = None):
        self.name:      str = player_name
        self.game:      PokerGame = poker_game
        self.id:        str = ""
        self._chips:    int = 0

        self._pocket_cards: List[Card, Card] = []

        self._all_in:   bool = False

    def setup_pregame(self):
        """
        This method is called when a game begins. Set starting amount of money etc.
        """
        raise NotImplementedError

    def clear_pocket_cards(self):
        self._pocket_cards.clear()

    def set_pocket_cards(self, cards: List[Card]):
        if not len(cards) == 2:
            raise Player.PocketCardException("player can only be given 2 pocket cards")
        self._pocket_cards.clear()
        self._pocket_cards.extend(cards)

    def player_to_left(self) -> Player:
        """
        Used to get the next player, i.e. player to the left of the this player
        """
        raise NotImplementedError

    def get_player_action(self) -> PlayerAction:
        """
        Returns a PlayerAction object, indicating the type of action and an associated value for raises
        """
        raise NotImplementedError

    def pay_blind(self) -> int:
        """
        Called when a Player needs to pay a big or small blind. Error if this player doesn't need to pay a blind
        TODO: This should all just be handled with a single transaction() method. Logic of why payments are needed
              should be kept in PokerGame
        """
        if self is self.game.players("small_blind"):
            blind = self.game.small_blind()
        elif self is self.game.players("big_blind"):
            blind = self.game.big_blind()
        else:
            raise Player.BlindException("Player {} is not currently a blind".format(self.name))
        return self._pay(blind)

    def pay_bet(self, amount: int) -> int:
        """
        Subtracts the bet amount from this players available money, and returns the money that the player wants to bet
        TODO: This should all just be handled with a single transaction() method. Logic of why payments are needed
              should be kept in PokerGame
        """
        return self._pay(amount)

    def _pay(self, amount: int) -> int:
        """
        Internal payment from this players chip store. If he cannot afford the payment, we are ALL IN
        """
        to_pay = min(self._chips, amount)
        self._chips -= to_pay
        self._all_in = self._chips == 0
        return to_pay

    class BlindException(BaseException):
        pass

    class PocketCardException(BaseException):
        pass


class PlayerAction:
    """
    Represents an action which can be taken by the user.
    Used to communicate to the PokerGame what the player wants to do.
    """
    ACTIONS = ("checkfold",
               "fold",
               "check",
               "see",
               "raise",
               "allin")

    def __init__(self, player: Player):
        self.id_player = player.id
        self._action = "checkfold"
        self.value = 0

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        if value not in PlayerAction.ACTIONS:
            raise PlayerAction.InputException("unknown input type")
        self._action = value

    class InputException(BaseException):
        pass
