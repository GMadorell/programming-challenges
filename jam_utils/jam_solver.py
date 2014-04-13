from abc import abstractmethod


class JamSolver(object):
    def __init__(self, output_path="output.txt"):
        """
        :param output_path: location of the file where the solutions will be stored.
        """
        self.__output_path = output_path

    def solve(self, instances):
        solutions = []
        for instance in instances:
            solutions.append(self.solve_instance(instance))

        with open(self.__output_path, "w") as output_file:
            for i, solution in enumerate(solutions, start=1):
                newline_needed = True if i != len(solutions) else False
                output_file.write("Case #{0}: {1}{2}".format(i, solution, "\n" if newline_needed else ""))

    @abstractmethod
    def solve_instance(self, instance):
        """
        Where the magic happens.
        This method should return the solution (as a string) of the given instance.
        """
        pass
