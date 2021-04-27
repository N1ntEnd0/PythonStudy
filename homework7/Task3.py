"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    # 00 01 02
    if board[0][0] == board[0][1] == board[0][2]:
        return f"{board[0][0]} wins!"
    # 10 11 12
    elif board[1][0] == board[1][1] == board[1][2]:
        return f"{board[1][0]} wins!"
    # 20 21 22
    elif board[2][0] == board[2][1] == board[2][2]:
        return f"{board[2][0]} wins!"
    # 00 10 20
    elif board[0][0] == board[1][0] == board[2][0]:
        return f"{board[0][0]} wins!"
    # 01 11 21
    elif board[0][1] == board[1][1] == board[2][1]:
        return f"{board[0][1]} wins!"
    # 02 12 22
    elif board[0][2] == board[1][2] == board[2][2]:
        return f"{board[0][2]} wins!"
    # 00 11 22
    elif board[0][0] == board[1][1] == board[2][2]:
        return f"{board[1][1]} wins!"
    # 02 11 20
    elif board[0][2] == board[1][1] == board[2][0]:
        return f"{board[0][2]} wins!"

    for i in board:
        for j in i:
            if j == "-":
                return "unfinished"

    return "draw!"
