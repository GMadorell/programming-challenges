#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
from Queue import PriorityQueue
import sys
import math
import numpy
from pprintpp import pprint
from scipy.spatial.distance import cityblock


class TuentiRestructurationSolver(object):
    def __init__(self, output_file=sys.stdout):
        self.__output_file = output_file
        self.solutions = []

    def solve(self, instances):
        solutions = []
        for i, instance in enumerate(instances, start=1):
            solutions.append(self.solve_instance(instance, i))

        for i, solution in enumerate(solutions, start=1):
            newline_needed = True if i != len(solutions) else False
            self.__output_file.write("{1}{2}".format(i, solution, "\n" if newline_needed else ""))

    def solve_instance(self, instance, instance_id):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        initial = instance.initial_table
        objective = instance.objective

        with open("DEBUG.txt", "a") as fd:
            fd.write("Instance: {0}\n {1}\n{2}\n------\n".format(instance_id, initial, objective))

        translator = self.get_translator(initial)
        initial = self.to_array(initial, translator)
        try:
            objective = self.to_array(objective, translator)
        except KeyError:
            return -1

        with open("DEBUG.txt", "a") as fd:
            fd.write("Instance: {0}\n {1}\n{2}\n------\n".format(instance_id, initial, objective))

        hard_heuristic_sol = \
            self.solve_heuristic(initial, objective, lambda actual, target: euclidean(actual, target) / 1.4)
        return "{0}".format(hard_heuristic_sol)

    def get_translator(self, initial):
        translations = {}
        count = 1
        for row in initial:
            for item in row:
                if item:
                    translations[item] = count
                    count += 1
                else:
                    translations[item] = 0
        return translations

    def to_array(self, initial, translator):
        as_array = numpy.zeros((3, 3), dtype=numpy.int8)

        for i in range(len(initial)):
            for j in range(len(initial)):
                as_array[i][j] = translator[initial[i][j]]

        return as_array

    def solve_heuristic(self, initial, objective, heuristic):
        initial_state = State(initial, 0, None, heuristic)

        # print("Initial heuristic: {0}".format(initial_state.calculate_heuristic(objective)))

        q = StatePriorityQueue(objective)
        q.add_state(initial_state)

        while True:
            state = q.consume()
            if state.is_final(objective):
                break

            for new_state in state.expand():
                q.add_state(new_state)

        # print("\n-----\n".join(map(lambda st: str(st), state.get_way_until_this_state())))

        return state.n_moves_made


class State(object):
    def __init__(self, position=None, n_moves_made=None, previous_state=None, heuristic=None):
        self.position = position
        self.n_moves_made = n_moves_made
        self.previous_state = previous_state
        self.h = heuristic

    def calculate_heuristic(self, target):
        return self.h(self.position, target) + self.n_moves_made
        # return self.n_moves_made

    def is_final(self, target):
        return manhattan_2d(self.position, target) == 0

    def expand(self):
        """ Returns the new states we can reach from this state. """
        # print self.position
        states = []
        # Top left corner.
        states.append(self.create_modification((0, 0), (0, 1)))
        states.append(self.create_modification((0, 0), (1, 0)))

        # Top right corner.
        states.append(self.create_modification((0, 2), (0, 1)))
        states.append(self.create_modification((0, 2), (1, 2)))

        # Bot left corner.
        states.append(self.create_modification((2, 0), (2, 1)))
        states.append(self.create_modification((2, 0), (1, 0)))

        # Bot right corner.
        states.append(self.create_modification((2, 2), (2, 1)))
        states.append(self.create_modification((2, 2), (1, 2)))

        # Middle cells - clockwise starting from north.
        states.append(self.create_modification((0, 1), (1, 1)))
        states.append(self.create_modification((1, 2), (1, 1)))
        states.append(self.create_modification((2, 1), (1, 1)))
        states.append(self.create_modification((1, 0), (1, 1)))

        # pprint(map(lambda state: state.position, states))
        return states

    def create_modification(self, from_coords, to_coords):
        new_pos = self.position.copy()
        x1, y1 = from_coords
        x2, y2 = to_coords
        new_pos[x1, y1], new_pos[x2, y2] = new_pos[x2, y2], new_pos[x1, y1]

        return State(new_pos, self.n_moves_made + 1, self, self.h)

    def get_way_until_this_state(self):
        """ Debug method. """
        if self.previous_state is None:
            return [self.position]
        return self.previous_state.get_way_until_this_state() + [self.position]


class StateHistory(object):
    def __init__(self):
        self.history = []

    def add(self, array):
        self.history.append(array)

    def __contains__(self, check_state):
        for state in self.history:
            if not numpy.array_equal(state.position, check_state.position):
                return False
        return True

    def find_equal_position_state(self, check_state):
        for state in self.history:
            if numpy.array_equal(state.position, check_state.position):
                return state
        raise LookupError("Not found")

    def delete(self, state):
        self.history.remove(state)


class StatePriorityQueue(object):
    def __init__(self, objective):
        self.q = PriorityQueue()
        self.objective = objective

    def consume(self):
        assert not self.q.empty()
        return self.q.get()[1]

    def add_state(self, state):
        self.q.put((state.calculate_heuristic(self.objective), state))


def manhattan_2d(first, second):
    manh = 0
    for i in range(len(second)):
        for j in range(len(second)):
            # if second[i, j] != 0:  # Remove 'if' if you want a full calculation.
            x, y = numpy.nonzero(first == second[i, j])
            #
            # # print x, y, i, j
            # print abs(x[0] - i) + abs(y[0] - j)
            manh += abs(x[0] - i) + abs(y[0] - j)

    return manh


def euclidean(first, second):
    euc = 0
    for i in range(len(second)):
        for j in range(len(second)):
            # if second[i, j] != 0:  # Remove 'if' if you want a full calculation.
            x, y = numpy.nonzero(first == second[i, j])
            euc += math.sqrt((x[0] - i) ** 2 + (y[0] - j) ** 2)
    return euc


class TuentiRestructurationInstance(object):
    def __init__(self):
        self.initial_table = None
        self.objective = None


class TuentiRestructurationParser(object):
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
        for i in range(0, len(self.data), 8):
            instance = TuentiRestructurationInstance()

            initial_table = []
            initial_table.append(map(lambda s: s.strip(), self.data[i + 1].split(",")))
            initial_table.append(map(lambda s: s.strip(), self.data[i + 2].split(",")))
            initial_table.append(map(lambda s: s.strip(), self.data[i + 3].split(",")))
            instance.initial_table = initial_table

            objective_table = []
            objective_table.append(map(lambda s: s.strip(), self.data[i + 5].split(",")))
            objective_table.append(map(lambda s: s.strip(), self.data[i + 6].split(",")))
            objective_table.append(map(lambda s: s.strip(), self.data[i + 7].split(",")))
            instance.objective = objective_table

            self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = TuentiRestructurationParser()
    solver = TuentiRestructurationSolver()
    solver.solve(parser.instances)