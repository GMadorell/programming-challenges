
from __future__ import division

"""
Cookies!!!

You have 0 cookies at the start.
 - Earn 2 cookies/second.
 - Farm costs C cookies.
 - Farm gives F cookies/sec.

Objective: calculate the min amount of time needed to get to X cookies.

Input = C, F, X
Output = seconds.



Sample input and output
-------------------------------

Input

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Output

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762


"""


PATH_DATA = "B-large-practice.in"
PATH_OUTPUT = "output.txt"


# Parsing
with open(PATH_DATA, "r") as fd:
    data = fd.readlines()

data = data[1:]
data = map(lambda s: s.strip(), data)


class SuperCookieInstance(object):
    def __init__(self):
        self.farm_cost = None
        self.farm_production = None
        self.objective = None

instances = []
for row in data:
    instance = SuperCookieInstance()
    splitted_row = row.split()
    numeric_row = map(lambda s: float(s), splitted_row)

    instance.farm_cost = numeric_row[0]
    instance.farm_production = numeric_row[1]
    instance.objective = numeric_row[2]

    instances.append(instance)


### PROBLEM SOLVING
def solve_instance(instance):
    production = 2
    cost = instance.farm_cost
    farm_production = instance.farm_production
    objective = instance.objective
    elapsed_time = 0

    while True:
        # Need to calculate how much time do we need if we buy the farm.
        # And also how much time do we need if we don't do anything.

        # If time_buying < time_without_buying,
        #   then buy a farm and iterate again.
        # Else
        #   simply return how much time we need until we get to the objective.

        time_next_farm = cost / production

        time_buying_farm = time_next_farm + elapsed_time + objective / (production + farm_production)

        time_without_buying = elapsed_time + objective / production

        if time_buying_farm < time_without_buying:
            elapsed_time += time_next_farm
            production += farm_production
        else:
            elapsed_time += objective / production
            return elapsed_time


solutions = []
for instance in instances:
    solutions.append(solve_instance(instance))

with open(PATH_OUTPUT, "w") as output_file:
    for i, solution in enumerate(solutions, start=1):
        newline_needed = True if i != len(solutions) else False
        output_file.write("Case #{0}: {1}{2}".format(i, solution, "\n" if newline_needed else ""))
