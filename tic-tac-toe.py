#CSE 210 Tic Tac Toe
#Angela Slinker

import random
from pickle import TRUE

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


def print_game_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
