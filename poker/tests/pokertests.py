import unittest
from poker import PokerGame


class PokerTests(unittest.TestCase):
    def test_add_remove_players(self):
        p = PokerGame()
        p.add_player("1", "Keegan")
        self.assertEqual(len(p.all_player_ids), 1)

        p.remove_player("1")
        self.assertEqual(len(p.all_player_ids), 0)

        p.add_player("1", "Keegan")
        self.assertRaises(AssertionError, p.add_player, "1", "Keegan2")
        p.add_player("2", "Rebecca")
        p.add_player("3", "Tubby")

        print(p.player_to_left())

if __name__ == '__main__':
    unittest.main()
