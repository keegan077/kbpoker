import unittest
from cards import Card


class CardTestCase(unittest.TestCase):

    def test_card_constructor(self):
        self.assertRaises(Card.RankException, Card, 0, "hearts")
        self.assertRaises(Card.SuitException, Card, 1, "shovels")

    def test_card_strings(self):
        self.assertEqual(str(Card(1, "clubs")), "Ace of Clubs")
        self.assertEqual(str(Card(7, "diamonds")), "Seven of Diamonds")
        self.assertEqual(str(Card(11, "hearts")), "Jack of Hearts")
        self.assertEqual(str(Card(12, "spades")), "Queen of Spades")

    def test_card_equality(self):
        self.assertEqual(Card(1, "hearts"), Card(1, "hearts"))
        self.assertNotEqual(Card(1, "hearts"), Card(2, "hearts"))
        self.assertNotEqual(Card(1, "hearts"), Card(1, "spades"))


if __name__ == '__main__':
    unittest.main()
