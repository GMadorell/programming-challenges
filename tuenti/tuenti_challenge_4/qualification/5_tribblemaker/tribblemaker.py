#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import numpy as np
import scipy.ndimage


ALIVE = 1
DEAD = 0


class TribblemakerSolver(object):
    def __init__(self, output_file=sys.stdout):
        self.__output_file = output_file

    def solve(self, instances):
        solutions = []
        for instance in instances:
            solutions.append(self.solve_instance(instance))

        for i, solution in enumerate(solutions, start=1):
            newline_needed = True if i != len(solutions) else False
            self.__output_file.write("{1}{2}".format(i, solution, "\n" if newline_needed else ""))

    def solve_instance(self, instance):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        self.conv_kernel = np.array([[1, 1, 1],
                                     [1, 10, 1],
                                     [1, 1, 1]])

        rows = instance.rows

        grid = self.initialize_grid(rows)

        loop_start, interval = self.find_game_of_life_repetitions(grid)

        return "{0} {1}".format(loop_start, interval)

    def initialize_grid(self, rows):
        grid = np.zeros((8, 8), dtype=np.int8)

        for i in range(len(rows)):
            for j in range(len(rows)):
                if rows[i][j].lower() == "x":
                    grid[i][j] = ALIVE

        return grid

    def find_game_of_life_repetitions(self, grid):
        """ Return: (generation at which the repetition start,
                     interval (in generations) between repetitions). """
        history = [grid]
        for generation in range(1, 102):
            grid = self.next_generation(grid)

            for old_generation, old_grid in enumerate(history):
                if np.array_equal(grid, old_grid):
                    return old_generation, generation - old_generation

            history.append(grid)
        else:
            raise Exception("Examples are guaranteed to repeate after 100 generations")

    def next_generation(self, grid):
        convolution = scipy.ndimage.filters.convolve(grid,
                                                     self.conv_kernel,
                                                     mode="constant")  # Change to wrap for real GoL.

        boolean = (convolution == 3) | (convolution == 12) | (convolution == 13)
        return np.int8(boolean)


class TribblemakerInstance(object):
    def __init__(self):
        self.rows = None


class TribblemakerParser(object):
    def __init__(self):
        data = sys.stdin.readlines()
        data = map(lambda s: s.strip(), data)

        self.data = data
        self.instances = []

        self.parse()

    def parse(self):
        """
        This method should populate the instances list.
        """
        rows = []
        instance = TribblemakerInstance()
        for line in self.data:
            row = line.strip()
            rows.append(list(row))
        instance.rows = rows
        self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = TribblemakerParser()
    solver = TribblemakerSolver()
    solver.solve(parser.instances)