#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import networkx as nx
import matplotlib.pyplot as plt
import time


FINAL = "AwesomeVille"


class BenditoChaosSolver(object):
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
        graph = self.construct_graph(instance)

        flow = nx.ford_fulkerson_flow(graph, instance.city_name, FINAL)

        max_speed_kmh = 0
        for node, flow_dict in flow.items():
            if FINAL in flow_dict:
                max_speed_kmh += flow_dict[FINAL]

        seconds_in_a_hour = 3600
        meters_per_car = 5

        max_speed_ms = max_speed_kmh * (1000/1) * (1/seconds_in_a_hour)
        cars_per_second = max_speed_ms * (1/meters_per_car)
        cars_per_hour = cars_per_second * seconds_in_a_hour

        return "{0} {1:.0f}".format(instance.city_name, cars_per_hour)

    def construct_graph(self, instance):
        g = nx.DiGraph()
        speed = instance.get_speed_map()
        for road in instance.roads:
            g.add_nodes_from([road.from_, road.to])
            g.add_edge(road.from_, road.to, road_type=road.road_type, lanes=road.lanes_n,
                       capacity=int(speed[road.road_type] * road.lanes_n))

        return g


class BenditoChaosInstance(object):
    def __init__(self):
        self.city_name = None
        self.s_speed = None
        self.d_speed = None
        self.intersections_n = None
        self.roads = None

    def get_speed_map(self):
        return {
            "dirt": int(self.d_speed),
            "normal": int(self.s_speed)
        }


class Road(object):
    def __init__(self, from_=None, to=None, road_type=None, lanes_amount=None):
        self.from_ = from_
        self.to = to
        self.road_type = road_type
        self.lanes_n = lanes_amount


class BenditoChaosParser(object):
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
        i = 0
        while i < len(self.data):
            instance = BenditoChaosInstance()

            instance.city_name = self.data[i]
            instance.s_speed, instance.d_speed = map(lambda string: int(string), self.data[i + 1].split())
            instance.intersections_n, amount_roads = map(lambda string: int(string), self.data[i + 2].split())

            i += 3

            roads = []
            for j in range(i, i + amount_roads, 1):
                from_, to, road_type, lanes = self.data[j].split()
                roads.append(Road(from_, to, road_type, int(lanes)))
            instance.roads = roads

            i += amount_roads

            self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = BenditoChaosParser()
    solver = BenditoChaosSolver()
    solver.solve(parser.instances)