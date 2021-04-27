from Task3 import tic_tac_toe_checker


def test_x_won_vertically():
    board = [["-", "x", "o"], ["-", "x", "o"], ["o", "x", "-"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_won_horizontally():
    board = [["-", "-", "x"], ["-", "x", "x"], ["o", "o", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def x_won_diagonally():
    board = [["x", "o", "x"], ["x", "x", "o"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_unfinished_result():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "unfinished"


def test_draw():
    board = [["o", "x", "o"], ["o", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "draw!"
