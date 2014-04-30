
"""
Problem description.
"""

from __future__ import division
import sys

import editdistance
import networkx as nx
from networkx.algorithms.shortest_paths import shortest_path


class ShapeShiftersSolver(object):
    def __init__(self, output_file=sys.stdout):
        self.__output_file = output_file
        self.graph = None

    def solve(self, instances):
        solutions = []
        for instance in instances:
            solutions.append(self.solve_instance(instance))

        for i, solution in enumerate(solutions, start=1):
            newline_needed = True if i != len(solutions) else False
            self.__output_file.write("{1}".format(i, solution, "\n" if newline_needed else ""))

    def solve_instance(self, instance):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        self.graph = nx.Graph()

        self.add_nodes_to_graph(instance)
        self.add_edges_to_graph(instance)

        path = shortest_path(self.graph, instance.start, instance.end)
        return "->".join(path)

    def add_nodes_to_graph(self, instance):
        all_nodes = [instance.start] + [instance.end] + instance.intermediate
        for node in all_nodes:
            self.graph.add_node(node)

    def add_edges_to_graph(self, instance):
        all_nodes = [instance.start] + [instance.end] + instance.intermediate
        for i in range(len(all_nodes)):
            for j in range(len(all_nodes)):
                if i != j and editdistance.eval(all_nodes[i], all_nodes[j]) == 1:
                    self.graph.add_edge(all_nodes[i], all_nodes[j])


class ShapeShiftersInstance(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.intermediate = None


class ShapeShiftersParser(object):
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
        instance = ShapeShiftersInstance()
        instance.start = self.data[0]
        instance.end = self.data[1]
        instance.intermediate = self.data[2:] if len(self.data) > 2 else []
        self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = ShapeShiftersParser()
    solver = ShapeShiftersSolver()
    solver.solve(parser.instances)