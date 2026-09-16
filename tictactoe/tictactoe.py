"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    CountX = 0
    CountO = 0

    for row in range (len(board)):
        for col in range (len(board[row])):
            if board [row][col] == X:
                CountX += 1
            if board [row][col] == O:
                CountO += 1
    if  CountX > CountO :
        return O
    else:
        return X





def actions(board):
    allpossibleactions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                allpossibleactions.add((row, col))
    return allpossibleactions




def result(board, action):
    if action not in actions(board):
        raise Exception("Not a valid action")

    row , col =action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkRow(board , player):
    for row in range (len(board)):
        if board [row][0] ==player  and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board , player ):
    for col in range (len(board)):
        if board[0][col] == player and board [1][col] == player and board[2][col] == player:
            return True
    return False



def check1Diag (board , player):
    count = 0
    for row in range (len(board)):
        for col in range (len(board[row])):
            if row == col and board[row][col]==player:
                count +=1
    return count == 3



def check2Diag(board, player):
    count = 0
    size = len(board)

    for row in range(size):
        for col in range(size):
            if row + col == size - 1 and board[row][col] == player:
                count += 1

    return count == 3


def winner(board):
    if checkRow(board, X) or checkCol(board, X) or check1Diag(board, X) or check2Diag(board, X):
        return X
    if checkRow(board, O) or checkCol(board, O) or check1Diag(board, O) or check2Diag(board, O):
        return O
    return None


def terminal(board):
    if winner(board) is not None:
        return True


    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        best_value = -math.inf
        best_move = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action

        return best_move

    else:  # O's turn
        best_value = math.inf
        best_move = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

        return best_move
