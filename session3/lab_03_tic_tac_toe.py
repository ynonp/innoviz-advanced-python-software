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



# Then implement has_winner
# (when done write in chat so we'll know to proceed)

# Return True if somebody (X or O) won
# Use boolean masks, np.all, slices
def has_winner(board):
    for i in range(3):
        if np.all(row(board, i) == 'O') or np.all(row(board, i) == 'X'):
            return True

        if np.all(column(board, i) == 'O') or np.all(column(board, i) == 'X'):
            return True

    if (np.all(diag1(board) == 'O')) or (np.all(diag1(board) == 'X')):
        return True

    if (np.all(diag2(board) == 'O')) or (np.all(diag2(board) == 'X')):
        return True

    return False


