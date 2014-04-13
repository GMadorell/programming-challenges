from abc import abstractmethod


class JamParser(object):
    def __init__(self, path):
        with open(path, "r") as fd:
            data = fd.readlines()
        data = map(lambda s: s.strip(), data)

        self.amount_samples = int(data[0])
        self.data = data[1:]
        self.instances = []

        self.parse()

    @abstractmethod
    def parse(self):
        """
        This method should populate the instances list.
        """
        pass
