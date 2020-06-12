"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import GameBoard


def test_GameBoard():
    game = GameBoard(3, 3)
    assert callable(GameBoard)
    assert game.height == 3
    assert game.width == 3
    assert game.grid == [["S", " ", " "],
                         [" ", " ", " "],
                         [" ", " ", "F"]]
    assert game.currentRow == 0
    assert game.currentColumn == 0


def test_set_player_location():
    game = GameBoard(2, 2)
    assert game.height == 2
    assert game.width == 2
    assert game.currentRow == 0
    assert game.currentColumn == 0
    game.set_player_location()
    assert game.grid == [["O", " "],
                         [" ", "F"]]


def test_move_right():
    game = GameBoard(3, 5)
    assert callable(game.move_right)
    game.move_right()
    assert game.grid == [[".", ".", "O"],
                         [" ", " ", " "],
                         [" ", " ", " "],
                         [" ", " ", " "],
                         [" ", " ", "F"]]
    assert game.currentColumn == 2
    assert game.currentRow == 0


def test_can_move_right():
    game = GameBoard(3, 5)
    assert callable(game.can_move_right)
    game.move_right()
    assert game.can_move_right() == False


def test_move_down():
    game = GameBoard(3, 3)
    assert callable(game.move_down)
    game.move_down()
    assert game.grid == [[".", " ", " "],
                         [".", " ", " "],
                         ["O", " ", "F"]]
    assert game.currentColumn == 0
    assert game.currentRow == 2


def test_can_move_down():
    game = GameBoard(7, 13)
    assert callable(game.can_move_down)
    game.move_down()
    assert game.can_move_down() == False


def test_add_random_obstacles():
    game = GameBoard(3, 4)
    assert callable(game.add_random_obstacles)
    assert game.add_random_obstacles(10)
    assert game.grid == [["S", "X", "X"],
                         ["X", "X", "X"],
                         ["X", "X", "X"],
                         ["X", "X", "F"]]
    assert game.currentColumn == 0
    assert game.currentRow == 0
    assert game.add_random_obstacles() == False


def test_is_won_game():
    game = GameBoard(3, 3)
    assert callable(game.won_game)
    game.move_right()
    game.move_down()
    assert game.won_game()


def test_is_game_over():
    game = GameBoard(3, 3)
    assert callable(game.is_game_over)
    game.move_down()
    assert game.is_game_over() == False
