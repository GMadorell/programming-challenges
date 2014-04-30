#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import math


class GamblerCupSolver(object):
    def __init__(self, output_file=sys.stdout):
        self.__output_file = output_file

    def solve(self, instances):
        solutions = []
        for instance in instances:
            solutions.append(self.solve_instance(instance))

        for i, solution in enumerate(solutions, start=1):
            newline_needed = True if i != len(solutions) else False
            if solution.is_integer():
                self.__output_file.write("{1:.0f}{2}".format(i, solution, "\n" if newline_needed else ""))
            else:
                self.__output_file.write("{1:.2f}{2}".format(i, solution, "\n" if newline_needed else ""))

    def solve_instance(self, instance):
        return math.sqrt(instance.x * instance.x + instance.y * instance.y)


class GamblerCupInstance(object):
    def __init__(self):
        self.x = None
        self.y = None


class GamblerCupParser(object):
    def __init__(self):
        data = sys.stdin.readlines()
        data = map(lambda s: s.strip(), data)

        self.amount_samples = int(data[0][0])
        self.data = data[1:]
        self.instances = []

        self.parse()

    def parse(self):
        """
        This method should populate the instances list.
        """
        for line in self.data:
            row = line.strip().split()
            instance = GamblerCupInstance()
            instance.x = int(row[0])
            instance.y = int(row[1])
            self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = GamblerCupParser()
    solver = GamblerCupSolver()
    solver.solve(parser.instances)