#!/usr/bin/env python
"""
Problem description.
"""

from __future__ import division
import StringIO
import gzip
import socket
import sys


# class RandomPasswordSolver(object):
#     def __init__(self, output_file=sys.stdout):
#         self.__output_file = output_file
#
#     def solve(self, instances):
#         solutions = []
#         for instance in instances:
#             solutions.append(self.solve_instance(instance))
#
#         for i, solution in enumerate(solutions, start=1):
#             newline_needed = True if i != len(solutions) else False
#             self.__output_file.write("Case #{0}: {1}{2}".format(i, solution, "\n" if newline_needed else ""))
#
#     def solve_instance(self, instance):
#         """
#         Where the magic happens.
#         This method should return the solution (as a string) of the given instance.
#         """
#         return "Not Done!!!"
#
#
# class RandomPasswordInstance(object):
#     def __init__(self):
#         pass
#
#
# class RandomPasswordParser(object):
#     def __init__(self):
#         data = sys.stdin.readlines()
#         data = map(lambda s: s.strip(), data)
#
#         self.amount_samples = int(data[0][0])
#         self.data = data[1:]
#         self.instances = []
#
#         self.parse()
#
#     def parse(self):
#         """
#         This method should populate the instances list.
#         """
#         for line in self.data:
#             row = line.strip()
#             instance = RandomPasswordInstance()
#             self.instances.append(instance)
#
#     def get_data_as_type(self, type_):
#         return map(lambda row: map(lambda element: type_(element), row), self.data)
import itertools
import requests

DEBUG = True

if __name__ == "__main__":
    # parser = RandomPasswordParser()
    # solver = RandomPasswordSolver()
    # solver.solve(parser.instances)

    if DEBUG:
        inp = "23f393c0f8"
    else:
        data = sys.stdin.readlines()
        inp = data[0].strip()

    # request_data = inp.encode("hex")
    #
    # request_data = open("challenge.token", "r")

    # req = requests.get("http://random.contest.tuenti.net/?input={0}".format(request_data))

    requests_to_try = []

    hex_mapping = {
        "a": "10",
        "b": "11",
        "c": "12",
        "d": "13",
        "e": "14",
        "f": "15"
    }
    for i in range(10):
        hex_mapping[str(i)] = str(i)

    # # Hex mapping.
    # result = ""
    # for letter in inp:
    #     result += hex_mapping[letter]
    # requests_to_try.append(result)

    # # Remove letters.
    # result = ""
    # for letter in inp:
    #     try:
    #         result += str(int(letter))
    #     except:
    #         pass
    # requests_to_try.append(result)

    # # Only letters.
    # result = ""
    # for letter in inp:
    #     if not letter.isdigit():
    #         result += letter
    # requests_to_try.append(result)

    # Mayus???
    # requests_to_try.append(inp.upper())

    # Gzip? It was in the headers.
    # def gunzip_text(text):
    #     infile = StringIO.StringIO()
    #     infile.write(text)
    #
    #     with gzip.GzipFile(fileobj=infile, mode="r") as f:
    #         f.rewind()
    #         return f.read()
    #
    # print gunzip_text

    # Caesar hexadecimal coding.
    # number_to_hex = {}
    # for key, value in hex_mapping.items():
    #     number_to_hex[value] = key
    #
    # for i in range(len(number_to_hex.keys())):
    #     caesar = ""
    #     for letter in inp:
    #         n = int(hex_mapping[letter])
    #         new_n = (n + i) % 16
    #         caesar += number_to_hex[str(new_n)]
    #     requests_to_try.append(caesar)

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("random.contest.tuenti.net", 80))
    #
    # s.send("GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % ("/{0}".format(input), 80))
    # print s.recv(2048)

    for request in requests_to_try:
        req = requests.get("http://random.contest.tuenti.net/?input={0}".format(request))

        # print req.headers
        # print req.encoding
        # print req.content
        # print req.cookies.items()
        # print req.url
        # print req.history

        print "{}: {}".format(request, req.text)
        if "wrong" not in req.text.lower():
            with open("DEBUG.txt", "a") as fd:
                fd.write("{0}\n".format(request))
