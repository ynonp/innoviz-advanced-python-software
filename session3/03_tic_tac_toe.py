import numpy as np

board = np.array([
    [' ', ' ', ' '],
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
])

# return the row <row_index>
def row(board, row_index):
    return board[row_index, :]


# return the column <col_index>
def column(board, col_index):
    return board[:, col_index]


# return the first diagonal (' ', 'O', ' ')
def diag1(board):
    return board[[0, 1, 2], [0, 1, 2]]
    #return np.diag(board)


# return the second diagonal (' ', 'O', ' ')
def diag2(board):
    return board[[0, 1, 2], [2, 1, 0]]


# Return True if somebody (X or O) won
# Use boolean masks, np.all, slices
def has_winner(board):
    pass


