#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import numpy as np


CORNERS = ("\\", "/")
START = "#"


RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4
DIRECTIONS = (RIGHT, LEFT, UP, DOWN)
HORIZONTAL_DIRS = (RIGHT, LEFT)
VERTICAL_DIRS = (UP, DOWN)

NOTHING = 0


ROAD_TO_NUMBER = {
    "#": 1,
    "-": 2,
    "\\": 3,
    "/": 4,
    "|": 5
}

NUMBER_TO_ROAD = {NOTHING: " "}
for key, value in ROAD_TO_NUMBER.items():
    NUMBER_TO_ROAD[value] = key


class F1RacingTeamSolver(object):
    def __init__(self, output_file=sys.stdout):
        self.__output_file = output_file

    def solve(self, instances):
        matrix_size = 100
        solution = "Sorry, I Failed :("
        while matrix_size < 100000:
            try:
                solution = self.solve_instance(instances[0], matrix_size)
            except IndexError as e:
                pass
            matrix_size *= 2

        self.__output_file.write("{0}".format(solution))

    def solve_instance(self, instance, matrix_size=1000):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        road = instance.road

        race = np.zeros((matrix_size, matrix_size), dtype=np.int8)

        x = (len(race) // 2) - 1
        y = len(race) // 2
        direction = RIGHT

        road = self.unify_road(road)
        for character in road:
            x, y = self.update_coordinates(direction, x, y)
            race[len(race) - y][x] = self.format_character(character, direction)

            if character in CORNERS:
                direction = self.update_direction(character, direction)

        race = self.trim_race(race)

        return self.format_race(race)

    def unify_road(self, road):
        while road[0] != START:
            road = road[-1] + road[:-1]
        while road[-1] not in CORNERS:
            road = road[-1] + road[:-1]
        return road

    def update_coordinates(self, direction, x, y):
        if direction == RIGHT:
            x += 1
        elif direction == LEFT:
            x -= 1
        elif direction == UP:
            y += 1
        else:
            y -= 1
        return x, y

    def update_direction(self, corner, previous_direction):
        assert corner in CORNERS
        if previous_direction == RIGHT and corner == "\\":
            new_direction = DOWN
        elif previous_direction == RIGHT and corner == "/":
            new_direction = UP
        elif previous_direction == LEFT and corner == "\\":
            new_direction = UP
        elif previous_direction == LEFT and corner == "/":
            new_direction = DOWN

        elif previous_direction == UP and corner == "\\":
            new_direction = LEFT
        elif previous_direction == UP and corner == "/":
            new_direction = RIGHT
        elif previous_direction == DOWN and corner == "\\":
            new_direction = RIGHT
        elif previous_direction == DOWN and corner == "/":
            new_direction = LEFT
        return new_direction

    def format_character(self, character, direction):
        if character == "-" and direction in VERTICAL_DIRS:
            return ROAD_TO_NUMBER["|"]
        else:
            return ROAD_TO_NUMBER[character]

    def trim_race(self, race):
        """ Removes all the rows and columns that are full of zeros. """
        race = race[np.any(race != NOTHING, axis=1), :]  # Rows
        race = race[:, np.any(race != NOTHING, axis=0)]  # Columns
        return race

    def format_race(self, race):
        rep = ""
        for row in race:
            for element in row:
                rep += NUMBER_TO_ROAD[element]
            rep += "\n"
        rep = rep[:-1]
        return rep


class RoadPart(object):
    def __init__(self, road_part=None, width=None, height=None):
        self.road_part = road_part
        self.width = width
        self.height = height


class F1RacingTeamInstance(object):
    def __init__(self):
        self.road = None


class F1RacingTeamParser(object):
    def __init__(self):
        data = []
        for line in sys.stdin:
            data.append(line)

        # print "Data: {0}".format(data)
        data = map(lambda s: s.strip(), data)
        self.data = data
        self.instances = []

        self.parse()

    def parse(self):
        """
        This method should populate the instances list.
        """
        for line in self.data:
            row = line.strip()
            instance = F1RacingTeamInstance()
            instance.road = row
            self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    parser = F1RacingTeamParser()
    solver = F1RacingTeamSolver()
    solver.solve(parser.instances)