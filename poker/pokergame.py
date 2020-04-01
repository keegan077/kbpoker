from __future__ import annotations
from typing import Optional, Union, Tuple, List, Dict, Any, NoReturn
from enum import Enum
from itertools import cycle
from poker import Player
from cards import Deck, Card
import random


class PokerGame:

    def __init__(self):
        """
        Creates a PokerGame object, in a pending state, waiting for players to join.
        """
        self._game_state:       PokerGame.GameState = PokerGame.GameState.INITIALISING

        # all players, unlimited number
        self._players: Dict[str, Player] = {}

        # table of positions of each player, based on their id, size to be defined in begin_game method, and not changed afterwards!
        self._table: List[Optional[str]] = []

        # key players
        self._dealer:       Optional[Player] = None
        self._big_blind:    Optional[Player] = None
        self._small_blind:  Optional[Player] = None

        self._blinds: Dict[str, int] = {
            "small": 0,
            "big": 0,
        }

        self._deck:             Deck = Deck()
        self._ccards_hidden:    List[Card] = []
        self._ccards_visible:   List[Card] = []
        self._pot:              int = 0

    def add_player(self, player_id: str, player_name: str):
        """
        Adds a player to our game.
        """
        assert player_id not in self._players
        self._players[player_id] = Player(player_name, player_id)

    def remove_player(self, player_id: str):
        """
        Removes the given player from the room, and also from the table if he is sitting there
        """
        assert player_id in self._players
        self._players.pop(player_id)
        if player_id in self._table:
            self._table.remove(player_id)

    def begin_game(self, game_args: Dict[str, Any]):
        """
        Attempts to begin the game. If parameters are missing, error and return
        """
        # TODO: Check for all required args in game_args

        pass

    def queue_player_action(self, player_id: str, player_action: Player.Action):
        """
        Add a player action to the player action queue. If it is the current waiting on player, begin the execution loop
        """
        pass

    class ArgumentException(BaseException):
        pass

    class BeginGameException(BaseException):
        pass

    class GameState(Enum):
        INITIALISING = 1
        WAITING_FOR_PLAYERS = 2
        WAITING_FOR_PLAYER_ACTION = 3
        RUNNING = 4


