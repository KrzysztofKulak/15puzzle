import unittest

from game import Game, IllegalMoveError


class GameTestCase(unittest.TestCase):
    def test_creation_default_state(self):
        game = Game()
        expected_state = list(range(1, 16)) + [None]
        self.assertEqual(expected_state, game.state)

    def test_creation_custom_state(self):
        state = [None] + list(range(15, 0, -1))
        game = Game(state)
        self.assertEqual(state, game.state)

    def test_str_casting(self):
        game = Game()
        expected_string = "[1, 2, 3, 4]\n[5, 6, 7, 8]\n" \
                          "[9, 10, 11, 12]\n[13, 14, 15, None]"
        self.assertEqual(expected_string, str(game))

    def test_win_check_for_default(self):
        game = Game()
        self.assertTrue(game)
        self.assertTrue(game.is_won())

    def test_win_check_for_custom(self):
        initial_state = list(range(1, 15)) + [None, 15]
        game = Game(initial_state)
        self.assertFalse(game)
        self.assertFalse(game.is_won())
        game.state[14], game.state[15] = game.state[15], game.state[14]
        self.assertTrue(game)
        self.assertTrue(game.is_won())

    def test_legal_moves_corners(self):
        game = Game()
        game.move(12)
        self.assertEqual(None, game[11])
        self.assertEqual(12, game[15])
        game = Game()
        game.move(15)
        self.assertEqual(None, game[14])
        self.assertEqual(15, game[15])
        game = Game([None] + list(range(1, 16)))
        game.move(1)
        self.assertEqual(None, game[1])
        self.assertEqual(1, game[0])
        game = Game([None] + list(range(1, 16)))
        game.move(4)
        self.assertEqual(None, game[4])
        self.assertEqual(4, game[0])

    def test_legal_moves_middle(self):
        game = Game(list(range(1, 6)) + [None] + list(range(6, 16)))
        game.move(2)
        self.assertEqual(None, game[1])
        self.assertEqual(2, game[5])
        game = Game(list(range(1, 6)) + [None] + list(range(6, 16)))
        game.move(5)
        self.assertEqual(None, game[4])
        self.assertEqual(5, game[5])
        game = Game(list(range(1, 6)) + [None] + list(range(6, 16)))
        game.move(6)
        self.assertEqual(None, game[6])
        self.assertEqual(6, game[5])
        game = Game(list(range(1, 6)) + [None] + list(range(6, 16)))
        game.move(9)
        self.assertEqual(None, game[9])
        self.assertEqual(9, game[5])

    def test_illegal_moves(self):
        default_state = list(range(1, 16)) + [None]
        game = Game()
        for i in list(range(1, 12)) + [13, 14]:
            with self.assertRaises(IllegalMoveError):
                game.move(i)
            self.assertEqual(default_state, game.state)
        state = list(range(1, 6)) + [None] + list(range(6, 16))
        game = Game(state)
        for i in [1, 3, 4, 7, 8, 10, 11]:
            with self.assertRaises(IllegalMoveError):
                game.move(i)
            self.assertEqual(state, game.state)


if __name__ == '__main__':
    unittest.main()
