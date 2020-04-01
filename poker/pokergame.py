from typing import Optional, Union, Tuple, List, Dict, Any, NoReturn
from itertools import cycle
from poker import Player
from cards import Deck, Card
import random


class PokerGame:

    # maximum number of players
    MAX_SEATS = 8

    # possible values for blind increase method
    BLIND_INCREASE_METHODS = ("double",
                              "constant",
                              "manual")

    # codes for possible game states
    GAME_STATES = ("pending",
                   "pre-flop",
                   "flop",
                   "turn",
                   "river",
                   "showdown",
                   "post-showdown",
                   "finished")

    def __init__(self):
        """
        Creates a PokerGame object, in a pending state, waiting for players to join.
        """
        self._game_state:       str = "pending"
        self._round:            int = 0

        # all players
        self._players: List[Optional[Player], ...] = []

        # key players
        self._player: Dict[str, Optional[Player]] = {
            "dealer": None,
            "big_blind": None,
            "small_blind": None,
            "last_raise": None,
        }

        self._blinds: Dict[str, int] = {
            "small": 0,
            "big": 0,
        }

        self._deck:             Deck = Deck()
        self._ccards_hidden:    List[Card] = []
        self._ccards_visible:   List[Card] = []
        self._pot:              int = 0

    def players(self, kw="all") -> Union[List[Player, ...], Player]:
        """
        Returns a list of all players in the game
        This is the same as the _seats collection with all empty spaces removed
        """
        if kw == "all":
            return [player for player in self._players if player is not None]
        if kw not in self._player:
            raise PokerGame.ArgumentException("unknown player keyword")
        return self._player[kw]

    def small_blind(self) -> int:
        """
        Returns the current value of the small blind
        """
        return self._blinds["small"]

    def big_blind(self):
        """
        Returns the current value of the big blind
        """
        return self._blinds["big"]

    def community_cards(self) -> List:
        """
        Returns the community cards currently visible in the game
        """
        return list(self._ccards_visible)

    def play(self):
        """
        Attempts to begin the game, will fail if certain conditions are not met, e.g. no players
        """
        if self._game_state != "pending":
            raise PokerGame.BeginGameException("poker game is already running")

        elif len(self.players()) < 2:
            raise PokerGame.BeginGameException("not enough players")

        else:
            for player in self.players():
                player.setup_pregame()

            self._player["dealer"] = self.players()[0]
            self._loop()

    def _loop(self):
        """
        Game loop. Will exit under finish conditions: i.e. only one player left
        """
        game_running = True

        while game_running:

            ### Poker loop steps
            self._game_state = "pre-flop"
            self._round += 1

            # deal cards to all active players
            self._deal_round()

            ## pre-flop
            # update game state
            # betting round - first player to bet is left of big blind

            ## flop
            # flip 3 cards
            # betting round

            ## turn
            # flip one card
            # betting round

            ## river
            # flip one card
            # betting round

            ## showdown
            # only if more than one player still standing

            # award winnings to  last player standing

    def _deal_round(self) -> NoReturn:
        """
        Resets the deck, and deals out all cards to each player, and also the community cards.
        For simplicity, two cards are immediately dealt to each player, and no burns occur.
        """
        self._deck.reset()
        self._deck.shuffle()

        for player in self.players():
            player.set_pocket_cards(self._deck.deal(2))

        # community cards
        self._ccards_hidden.clear()
        self._ccards_visible.clear()
        self._ccards_hidden.extend(self._deck.deal(5))

    def get_bets(self, collect_blinds=False, collect_ante=False) -> int:
        """
        collects bets from all players. Returns the sum of all bets from all players to go in the pot
        """
        # players need to respond:
        # possible actions:
        # - fold:   player is OUT
        # - check:  player is in, but no bet. not valid if a raise has already occured
        # - see:    player bets as much as the current bet
        # - raise:  player bets as much as current bet, and increases

        if collect_blinds:
            # if we need to collect blinds, blinds have no choice but to raise
            pass

    class ArgumentException(BaseException):
        pass

    class BeginGameException(BaseException):
        pass