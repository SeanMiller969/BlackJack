from pydealer.deck import Deck
from pydealer.tools import build_cards
from collections import deque
from const import *

class BlackJackDeck(Deck):
    def __init__(self, **kwargs):
        self._cards = deque(kwargs.get("cards", []))

        self.jokers = kwargs.get("jokers", False)
        self.num_jokers = kwargs.get("num_jokers", 0)
        self.rebuild = kwargs.get("rebuild", True)
        self.re_shuffle = kwargs.get("re_shuffle", True)
        self.ranks = kwargs.get("ranks", BLACKJACK_RANKS)
        self.number_of_decks = kwargs.get("number_of_decks", 1)
        self.decks_used = 0

        self.build()

    def build(self):
        self.decks_used += self.number_of_decks

        for _ in range(self.number_of_decks):
            self.cards += build_cards()
