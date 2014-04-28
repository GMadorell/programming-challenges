#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import sys
import sqlite3

PATH_DATA = "students"


class AnonymousPollInstance(object):
    def __init__(self):
        self.gender = None
        self.age = None
        self.studies = None
        self.academic_year = None


class AnonymousPollSolver(object):
    def __init__(self, connection, output_file=sys.stdout):
        self.__output_file = output_file
        self.__connection = connection

    def solve(self, instances):
        solutions = []
        for instance in instances:
            solutions.append(self.solve_instance(instance))

        for i, solution in enumerate(solutions, start=1):
            newline_needed = True if i != len(solutions) else False
            self.__output_file.write("Case #{0}: {1}{2}".format(i, solution, "\n" if newline_needed else ""))

    def solve_instance(self, instance):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        cursor = self.__connection.cursor()

        cursor.execute(
            """
                SELECT student_name
                FROM STUDENTS
                WHERE gender = ? AND age = ? AND education = ? AND academic_year = ?
            """, (instance.gender, int(instance.age), instance.studies, int(instance.academic_year))
        )

        names = cursor.fetchall()

        if len(names) > 0:
            return ",".join(sorted(map(lambda item: str(item[0]), names)))
        else:
            return "NONE"


class AnonymousPollParser(object):
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
            row = line.strip().split(",")
            instance = AnonymousPollInstance()
            instance.gender = row[0]
            instance.age = row[1]
            instance.studies = row[2]
            instance.academic_year = row[3]
            self.instances.append(instance)

    def get_data_as_type(self, type_):
        return map(lambda row: map(lambda element: type_(element), row), self.data)


if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Students")

    cursor.execute("""
                   CREATE TABLE Students
                      (student_name TEXT, gender TEXT, age INTEGER, education TEXT, academic_year INTEGER)
                   """)

    with open(PATH_DATA, "r") as students_file:
        for line in students_file.readlines():
            name, gender, age, education, academic_year = line.strip().split(",")
            cursor.execute("INSERT INTO Students VALUES (?, ?, ?, ?, ?)",
                           (name, gender, age, education, academic_year))
    connection.commit()

    parser = AnonymousPollParser()
    solver = AnonymousPollSolver(connection)
    solver.solve(parser.instances)

    connection.close()