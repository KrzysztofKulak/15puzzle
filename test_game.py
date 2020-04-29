import unittest

from game import Game


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

    def test_win_check_for_custom(self):
        initial_state = list(range(1, 15)) + [None, 15]
        game = Game(initial_state)
        self.assertFalse(game)
        game.state[14], game.state[15] = game.state[15], game.state[14]
        self.assertTrue(game)


if __name__ == '__main__':
    unittest.main()
