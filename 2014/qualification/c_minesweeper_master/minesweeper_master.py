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
import itertools
from unittest import TestCase
from pprintpp import pprint
from jam_utils.jam_parser import JamParser
from jam_utils.jam_solver import JamSolver

PATH_DATA = "C-large-practice.in"
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


CLICK, MINE, CLEAN, NOT_POSSIBLE, NOTHING = range(5)


class MinesweeperMasterSolver(JamSolver):
    def fill_board_from_center_to_exterior(self, initial_col, initial_row, offset, spaces_to_fill):
        pass

    def solve_instance(self, instance):
        rows = instance.rows
        cols = instance.columns
        mines = instance.mines

        # Strategy:
        #   Put all the mines at the lower-right part of the grid and click on top-left.


        # Fill the mines


        initial_row = rows // 2
        initial_col = cols // 2

        offset = -1

        spaces_to_fill = rows * cols - mines

        only_one_space = cols * rows - mines == 1

        # Solve the edge case in which you win simply by clicking.
        if only_one_space:
            board = [list() for _ in xrange(rows)]
            for row in board:
                [row.append(MINE) for _ in range(cols)]
            board[0][0] = NOTHING
            return self.format_solution_board(board)

        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(NOTHING) for _ in range(cols)]

        self.fill_board_with_mines(board, cols, mines, rows)
        if self.is_one_click_win_possible(board, cols, mines, rows):
            return self.format_solution_board(board)

        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(MINE) for _ in range(cols)]

        # If that fails, try to fill the board from the middle to the exterior of it.
        while self.count_cells(board, NOTHING) < spaces_to_fill:

            offset += 1

            sliding_col = initial_col - offset - 1
            sliding_row = initial_row - offset

            while sliding_col < initial_col + offset:
                sliding_col += 1

                for row, col in itertools.product([sliding_row - 1, sliding_row, sliding_row + 1],
                                                  [sliding_col - 1, sliding_col, sliding_col + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)

            sliding_col = initial_col - offset
            sliding_row = initial_row - offset - 1

            while sliding_row < initial_row + offset:
                sliding_row += 1

                for row, col in itertools.product([sliding_row - 1, sliding_row, sliding_row + 1],
                                                  [sliding_col - 1, sliding_col, sliding_col + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)

            sliding_col = initial_col + offset
            sliding_row = initial_row - offset - 1

            while sliding_row < initial_row + offset:
                sliding_row += 1

                for row, col in itertools.product([sliding_row - 1, sliding_row, sliding_row + 1],
                                                  [sliding_col - 1, sliding_col, sliding_col + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)

            sliding_col = initial_col - offset - 1
            sliding_row = initial_row + offset

            while sliding_col < initial_col + offset:
                sliding_col += 1

                for row, col in itertools.product([sliding_row - 1, sliding_row, sliding_row + 1],
                                                  [sliding_col - 1, sliding_col, sliding_col + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)
        if self.is_one_click_win_possible(board, cols, mines, rows):
            return self.format_solution_board(board)

        i = 1

        # If that fails, try filling the board horizontally.
        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(MINE) for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                for row, col in itertools.product([i - 1, i, i + 1],
                                                  [j - 1, j, j + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)

        if self.is_one_click_win_possible(board, cols, mines, rows):
            return self.format_solution_board(board)

        i = 1

        # If that fails, try filling the board vertically.
        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(MINE) for _ in range(cols)]

        for j in range(cols):
            for i in range(rows):
                for row, col in itertools.product([i - 1, i, i + 1],
                                                  [j - 1, j, j + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, row, col, NOTHING)

        if self.is_one_click_win_possible(board, cols, mines, rows):
            return self.format_solution_board(board)

        i = 1

        # If we don't win by that, try
        board = [list() for _ in xrange(rows)]
        for row in board:
            [row.append(MINE) for _ in range(cols)]

        initial_row = rows
        initial_col = cols - 1

        while self.count_cells(board, NOTHING) != spaces_to_fill:

            if initial_row > 0:
                initial_row -= 1
            else:
                initial_col -= 1

            row = initial_row
            col = initial_col

            i = 1

            while row < rows and col >= 0:

                for expanded_row, expanded_col in itertools.product([row - 1, row, row + 1],
                                                                    [col - 1, col, col + 1]):
                    if self.count_cells(board, NOTHING) == spaces_to_fill:
                        break
                    self.set_board_status(board, expanded_row, expanded_col, NOTHING)

                row += 1
                col -= 1

        if self.is_one_click_win_possible(board, cols, mines, rows):
            return self.format_solution_board(board)
        else:
            return "\nImpossible"

    def fill_board_with_mines(self, board, cols, mines, rows):
        """
        Puts mines starting from bottom-right to top-left.
        """
        planted_mines = 0
        initial_row = rows
        initial_col = cols - 1

        row = rows - 1
        col = cols

        while planted_mines < mines:

            # col -= 1
            #
            # if col < 0:
            #     col = cols - 1
            #     row -= 1
            #
            # board[row][col] = MINE
            # planted_mines += 1

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
            if NOT_POSSIBLE in row or NOTHING in row:
                possible = False
                break

        only_one_space = cols * rows - mines == 1

        return possible or only_one_space

    def expand_board(self, board, cols, mines, rows):
        for row in range(rows):
            for column in range(cols):
                if not self.has_mine_nearby(board, row, column):
                    self.set_board_status(board, row - 1, column - 1, CLEAN)
                    self.set_board_status(board, row - 1, column, CLEAN)
                    self.set_board_status(board, row - 1, column + 1, CLEAN)
                    self.set_board_status(board, row, column - 1, CLEAN)
                    self.set_board_status(board, row, column, CLEAN)
                    self.set_board_status(board, row, column + 1, CLEAN)
                    self.set_board_status(board, row + 1, column - 1, CLEAN)
                    self.set_board_status(board, row + 1, column, CLEAN)
                    self.set_board_status(board, row + 1, column + 1, CLEAN)

    def has_mine_nearby(self, board, row, column):
        return self.get_board_status(board, row - 1, column - 1, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row - 1, column, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row - 1, column + 1, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row, column - 1, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row, column, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row, column + 1, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row + 1, column - 1, NOT_POSSIBLE) == MINE \
                   or self.get_board_status(board, row + 1, column, NOT_POSSIBLE) == MINE \
            or self.get_board_status(board, row + 1, column + 1, NOT_POSSIBLE) == MINE

    def get_board_status(self, board, row, col, outbounds_default):
        rows = len(board)
        cols = len(board[0])

        if not self.is_valid_position(rows, cols, row, col):
            return outbounds_default

        return board[row][col]

    def set_board_status(self, board, row, column, status):
        rows = len(board)
        cols = len(board[0])

        if self.is_valid_position(rows, cols, row, column):
            board[row][column] = status

    def is_valid_position(self, rows, cols, row, column):
        return 0 <= row <= rows - 1 and 0 <= column <= cols - 1

    def count_cells(self, board, status):
        return sum([len(filter(lambda cell_value: cell_value == status, row)) for row in board])

    def format_solution_board(self, board):
        rows, cols = len(board), len(board[0])

        click_row, click_col = 0, 0
        for row in range(rows):
            for col in range(cols):
                if not self.has_mine_nearby(board, row, col):
                    click_row, click_col = row, col

        solution_str = "\n"

        for row in range(rows):
            for col in range(cols):
                if row == click_row and col == click_col:
                    solution_str += "c"
                elif board[row][col] == MINE:
                    solution_str += "*"
                elif board[row][col] == CLEAN:
                    solution_str += "."
            solution_str += "\n"

        solution_str = solution_str[:-1]  # Remove last \n

        return solution_str


class MinesweeperTests(TestCase):
    def test_initial(self):
        self.instance_test(5, 5, 23, False)
        self.instance_test(3, 1, 1, True)
        self.instance_test(2, 2, 1, False)
        self.instance_test(4, 7, 3, True)
        self.instance_test(10, 10, 82, True)

    def tests_small(self):
        self.instance_test(1, 4, 0, True)

    def test_3_3_5(self):
        self.instance_test(3, 3, 5, True)

    def test_one_free_space(self):
        self.instance_test(2, 1, 1, True)
        self.instance_test(3, 1, 2, True)

    # def test_5_5_14(self):
    #     self.instance_test(5, 5, 14, True)

    def test_4_3_2(self):
        self.instance_test(4, 3, 2, True)

    def test_4_5_4(self):
        self.instance_test(4, 5, 4, True)

    def test_5_5_14(self):
        self.instance_test(5, 5, 14, True)

    def test_5_5_9(self):
        self.instance_test(5, 5, 9, True)

    def instance_test(self, rows, cols, mines, is_possible):
        instance = MinesweeperMasterInstance()
        instance.rows, instance.columns, instance.mines = rows, cols, mines

        solver = MinesweeperMasterSolver()
        solution = solver.solve_instance(instance)

        if is_possible:
            assert "Impossible" not in solution, "Failed: %d %d %d should be possible." % (rows, cols, mines)
        else:
            assert "Impossible" in solution, "Failed: %d %d %d should be impossible." % (rows, cols, mines)


if __name__ == "__main__":
    parser = MinesweeperMasterParser(PATH_DATA)
    solver = MinesweeperMasterSolver(PATH_OUTPUT)
    solver.solve(parser.instances)