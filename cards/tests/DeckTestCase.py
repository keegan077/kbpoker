import unittest
from cards import Deck


class DeckTestCase(unittest.TestCase):

    def test_deck_overdeal(self):
        deck = Deck()
        self.assertRaises(Deck.DealException, Deck.deal, deck, 53)

    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

        deck.deal()
        self.assertEqual(len(deck), 51)

        deck.deal(2)
        self.assertEqual(len(deck), 49)


if __name__ == '__main__':
    unittest.main()
