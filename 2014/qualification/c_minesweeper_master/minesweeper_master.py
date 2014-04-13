
"""
Minesweeper - https://code.google.com/codejam/contest/2974486/dashboard#s=p2
-----------------

- You play on a grid of cells with hidden content.
- There are M hidden mines, in M hidden cells, and no other cells contain mines.
- Clicking a cell reveals it.
    - Click on a mine = lose.
    - If no mine -> Number appears, [0-8], indicating amount on mines next to it.
        - If number is 0 -> Neighbour cells are recursively revealed.
- Win condition: when all cells that don't contain mines are revealed.


Your job is: given a grid configuration, to output a mine distribution in which you
can win clicking only once.
If that's not possible, output "Impossible".

For each test case, output a line containing "Case #x:", where x is the test case number
(starting from 1).
On the following R lines, output the board configuration with C characters per line,
using '.' to represent an empty cell, '*' to represent a cell that contains a mine,
and 'c' to represent the clicked cell.

Input = R, C, M.
    R = rows
    C = columns
    M = number of hidden mines.


Sample input:
-----------------
5
5 5 23
3 1 1
2 2 1
4 7 3
10 10 82

Sample output:
-----------------
Case #1:
Impossible
Case #2:
c
.
*
Case #3:
Impossible
Case #4:
......*
.c....*
.......
..*....
Case #5:
**********
**********
**********
****....**
***.....**
***.c...**
***....***
**********
**********
**********
"""

from __future__ import division
from jam_utils.jam_parser import JamParser
from jam_utils.jam_solver import JamSolver

PATH_DATA = "data.txt"
PATH_OUTPUT = PATH_DATA.split(".")[0] + ".out"  # Same name as path data, except for the file format.


class MinesweeperMasterInstance(object):
    def __init__(self):
        self.rows = None
        self.columns = None
        self.mines = None


class MinesweeperMasterParser(JamParser):
    def parse(self):
        """
        This method needs to fill the instances list.
        """
        # self.data is a list of rows. every row is a row of the input file
        # already split as str.
        # use self.get_data_as_type() to parse it to a different type if needed.
        for row in self.get_data_as_type(int):
            instance = MinesweeperMasterInstance()
            instance.rows, instance.columns, instance.mines = row
            self.instances.append(instance)

CLICK, MINE, CLEAN, NOTHING = range(4)


class MinesweeperMasterSolver(JamSolver):
    def solve_instance(self, instance):
        rows = instance.rows
        cols = instance.columns
        mines = instance.mines

        # Strategy:
        #   Put all the mines at the lower-right part of the grid and click on top-left.
        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(NOTHING) for _ in range(cols)]

        # Fill the mines
        self.fill_board_with_mines(board, cols, mines, rows)

        possible = self.is_one_click_win_possible(board, cols, mines, rows)

    def fill_board_with_mines(self, board, cols, mines, rows):
        """
        Puts mines starting from bottom-right to top-left.
        """
        planted_mines = 0
        initial_row = rows
        initial_col = cols - 1

        while planted_mines < mines:

            if initial_row > 0:
                initial_row -= 1
            else:
                initial_col -= 1

            row = initial_row
            col = initial_col

            while row < rows and col >= 0:
                assert board[row][col] != MINE, \
                    "Repetition - Tryed to put a mine in a cell in which a mine already existed."
                board[row][col] = MINE
                planted_mines += 1
                row += 1
                col -= 1
                if planted_mines == mines:
                    break

    def is_one_click_win_possible(self, board, cols, mines, rows):
        self.expand_board(board, cols, mines, rows)

        possible = True

        for row in board:
            if NOTHING in row:
                possible = False
                break

        print possible

    def expand_board(self, board, cols, mines, rows):
        for row in range(rows):
            for column in range(cols):
                if not self.has_mine_nearby(board, row, column):
                    board[row][column] = CLEAN
                    # Missing: set the nearby cells to CLEAN.

    def has_mine_nearby(self, board, row, column):
        return self.get_board_status(board, row - 1, column - 1, NOTHING) == MINE \
            or self.get_board_status(board, row - 1, column,     NOTHING) == MINE \
            or self.get_board_status(board, row - 1, column + 1, NOTHING) == MINE \
            or self.get_board_status(board, row,     column - 1, NOTHING) == MINE \
            or self.get_board_status(board, row,     column,     NOTHING) == MINE \
            or self.get_board_status(board, row,     column + 1, NOTHING) == MINE \
            or self.get_board_status(board, row + 1, column - 1, NOTHING) == MINE \
            or self.get_board_status(board, row + 1, column,     NOTHING) == MINE \
            or self.get_board_status(board, row + 1, column + 1, NOTHING) == MINE

    def get_board_status(self, board, row, col, outbounds_default):
        rows = len(board)
        cols = len(board[0])

        if not 0 <= row <= rows - 1 or not 0 <= col <= cols - 1:
            return outbounds_default

        return board[row][col]


if __name__ == "__main__":
    parser = MinesweeperMasterParser(PATH_DATA)
    solver = MinesweeperMasterSolver(PATH_OUTPUT)
    solver.solve(parser.instances)