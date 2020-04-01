from __future__ import annotations
from typing import Optional, Union, Tuple, List, Dict, Any, NoReturn
from enum import Enum
from poker import Player, PlayerAction
from cards import Deck, Card


class PokerGame:

    def __init__(self):
        """
        Creates a PokerGame object, in a pending state, waiting for players to join.
        """
        self._game_state = PokerGame.GameState.INITIALISING
        self._round_state = PokerGame.RoundState.END

        # all players, unlimited number
        self._players: Dict[str, Player] = {}

        # table of positions of each player, based on their id
        # size to be defined in begin_game method, and not changed afterwards!
        self._table: List[Optional[str]] = []

        # key players
        self._dealer:       Optional[Player] = None
        self._big_blind:    Optional[Player] = None
        self._small_blind:  Optional[Player] = None

        # Game properties
        self._blinds_small: int = 0
        self._blinds_big:   int = 0

        self._player_action_queue: Dict[str, PlayerAction] = {}

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

    def _begin_round(self):
        """
        Called when a new round should be started.
        After this method returns, property for current_turn will have the player id of the player whose input is needed
        """
        pass

    def _pre_flop(self):
        pass

    def _flop(self):
        pass

    def _turn(self):
        pass

    def _river(self):
        pass

    def _end_round(self):
        pass

    def process_player_actions(self):
        """
        Searches in our collection of player actions for the current player action, and executes each
        """
        player_current_turn = self.get_player_current_turn()

    def get_player_current_turn(self):
        assert self._game_state == PokerGame.GameState.WAITING_FOR_PLAYER_ACTION, "game is not waiting for player input"
        assert self

    def queue_player_action(self, player_id: str, player_action: PlayerAction):
        """
        Add a player action to the player action queue. If it is the current waiting on player, begin the execution loop
        """
        self._player_action_queue[player_id] = player_action

    class GameState(Enum):
        INITIALISING = 1
        WAITING_FOR_PLAYERS = 2
        WAITING_FOR_PLAYER_ACTION = 3
        RUNNING = 4

    class RoundState(Enum):
        PREFLOP = 1
        FLOP = 2
        TURN = 3
        RIVER = 4
        END = 5



