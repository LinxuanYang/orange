"""Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
"""


def countbattleship(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x' and ((i == 0) or board[i][j-1] == '.') and ((j == 0)or board[i-1][j] == '.'):
                count += 1
    return count


board = [['.', 'x', '.', 'x', 'x'], ['.', 'x', '.', '.', '.'], ['x', '.', 'x', 'x', 'x'], ['.', 'x', '.', '.', '.'],
         ['x', '.', 'x', '.', '.']]
print(countbattleship(board))
