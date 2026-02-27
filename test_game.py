from game import Game


def test_initial_board():
    game = Game()
    assert len(game._board) == 9
    assert all(field == " " for field in game._board)


def test_winner_row():
    game = Game()
    game._board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert game._check_winner() == "X"


def test_winner_column():
    game = Game()
    game._board = [
        "O", " ", " ",
        "O", " ", " ",
        "O", " ", " "
    ]
    assert game._check_winner() == "O"


def test_winner_diagonal():
    game = Game()
    game._board = [
        "X", " ", " ",
        " ", "X", " ",
        " ", " ", "X"
    ]
    assert game._check_winner() == "X"


def test_no_winner():
    game = Game()
    game._board = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]
    assert game._check_winner() is None
