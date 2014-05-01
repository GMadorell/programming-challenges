#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import networkx
from networkx.algorithms.shortest_paths import shortest_path, has_path, all_shortest_paths


class YesWeScanSolver(object):
    def __init__(self, log_graph, output_file=sys.stdout):
        self.__output_file = output_file
        self.log_graph = log_graph

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
        id1, id2 = instance.id_start, instance.id_end

        if not has_path(self.log_graph, id1, id2):
            return "Not connected"

        cutoff = 25
        path = min(networkx.all_simple_paths(self.log_graph, id1, id2, cutoff=cutoff),
                   key=lambda p: self.find_max_id(p))

        call_id = self.find_max_id(path)

        return "Connected at {0}".format(call_id)

    def find_max_id(self, path):
        latest_call = max(pairwise(path), key=lambda pair: self.log_graph[pair[0]][pair[1]]["call_id"])
        return self.log_graph[latest_call[0]][latest_call[1]]["call_id"]


def pairwise(iterable):
    for i in xrange(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


class YesWeScanInstance(object):
    def __init__(self):
        self.id_start = None
        self.id_end = None


class YesWeScanParser(object):
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
        instance = YesWeScanInstance()
        instance.id_start = int(self.data[0])
        instance.id_end = int(self.data[1])

        self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":

    graph = networkx.Graph()

    with open("phone_call.log", "r") as log:
        for i, line in enumerate(log):
            id1, id2 = map(lambda string: int(string), line.strip().split())
            if not graph.has_node(id1):
                graph.add_node(id1)
            if not graph.has_node(id2):
                graph.add_node(id2)
            if not graph.has_edge(id1, id2):
                graph.add_edge(id1, id2, call_id=i)

    parser = YesWeScanParser()
    solver = YesWeScanSolver(graph)
    solver.solve(parser.instances)
