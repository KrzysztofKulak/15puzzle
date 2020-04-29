from random import randint, choice

from game import Game, IllegalMoveError


def set_random_state(game):
    """ since random states that cannot be achieved by moving
    the tile around exist (unsolvable states), random.shuffle
    cannot be used, instead random moves are applied to create
    random state achievable by moving the tiles around """
    for _ in range(1, randint(10, 10000)):
        try:
            game.move(game[game.empty_field + choice([-4, -1, 1, 4])])
        except (IllegalMoveError, IndexError):
            pass


game = Game()
set_random_state(game)
print(game)
while not game.is_won():
    try:
        tile = int(input("select tile to move: "))
        game.move(tile)
        print(game)
    except IllegalMoveError:
        print("Selected tile is not adjacent to the empty space")
    except ValueError:
        print("Wrong value provided")
print("congratz")
