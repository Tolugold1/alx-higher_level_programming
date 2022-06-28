#!/usr/bin/python3
from sys import argv


class Chessboard:
    """Represents a chessboard."""
    def __init__(self, size):
        """Initialize the data."""
        self.size = size
        self.cols = []

    def place_in_next_row(self, col):
        """Place in next row."""
        self.cols.append(col)

    def remove_in_current_row(self):
        """Remove in current row."""
        return self.cols.pop()

    def next_row_safe(self, col):
        """Check if current col in the next row is safe."""
        row = len(self.cols)
        for q_col in self.cols:
            if col == q_col:
                return False

        for q_row, q_col in enumerate(self.cols):
            if q_col - q_row == col - row:
                return False

        for q_row, q_col in enumerate(self.cols):
            if self.size - q_col - q_row == self.size - col - row:
                return False

        return True

    def display(self):
        """Display a valid solution."""
        print('[', end='')
        for row in range(self.size):
            for col in range(self.size):
                if col == self.cols[row]:
                    print('[{}, {}]'.format(row, col), end='')
                    if row < self.size - 1:
                        print(', ', end='')
        print(']')


def solve(size):
    """Solve the N queens problem."""
    board = Chessboard(size)
    row = col = 0
    while True:
        while col < size:
            if board.next_row_safe(col):
                board.place_in_next_row(col)
                row += 1
                col = 0
                break
            else:
                col += 1

        if col == size or row == size:
            if row == size:
                board.display()
                board.remove_in_current_row()
                row -= 1

            try:
                prev_col = board.remove_in_current_row()
            except IndexError:
                break

            row -= 1
            col = 1 + prev_col


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    queens = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if queens < 4:
    print('N must be at least 4')
    exit(1)

solve(queens)
