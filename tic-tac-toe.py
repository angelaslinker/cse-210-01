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

def main():
    while gameRunning:
        print_game_board(board)
        playerinput(board)
        check_winner(board)
        check_tie(board)
        switchPlayer()
        computer_player(board)
        check_winner(board)
        check_tie(board)


def print_game_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

#getting the players input
def playerinput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print('Try again!')
#checking for win or tie
def check_across(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[5] == board[6] == board[7] and board[6] != "-":
        winner = board[5]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
    
def check_horizontle(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True
def check_winner(board):
    global gameRunning
    if check_across(board):
        print_game_board(board)
        print(f"The winner is {winner}")
        gameRunning = False

    elif check_row(board):
        print_game_board(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif check_horizontle(board):
        print_game_board(board)
        print(f"The winner is {winner}!")
        gameRunning = False

def check_tie(board):
    global gameRunning
    if '-' not in board:
        print_game_board(board)
        print('It is a tie!')
        gameRunning = False
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer_player(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

if __name__ == "__main__":
    main()

