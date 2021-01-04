import numpy as np
import session3.lab_03_tic_tac_toe as game

def test_xxx_on_first_row():
    board = np.array([
        ['X', 'X', 'X'],
        ['O', ' ', ' '],
        [' ', ' ', ' ']
    ])
    assert game.has_winner(board) == True


def test_o_wins_in_diagonal():
    board = np.array([
        ['O', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', 'O']
    ])
    assert game.has_winner(board) == True


def test_x_wins_in_last_column():
    board = np.array([
        ['O', 'X', 'X'],
        ['O', 'O', 'X'],
        [' ', ' ', 'X']
    ])
    assert game.has_winner(board) == True

def test_tie():
    board = np.array([
        ['O', 'X', 'O'],
        ['O', 'O', 'X'],
        ['X', 'O', 'X']
    ])
    assert game.has_winner(board) == False


def test_x_wins_board_full():
    board = np.array([
        ['X', 'X', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ])
    assert game.has_winner(board) == True

