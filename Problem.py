import numpy as np

from Configuration import Configuration


class Problem:
    def __init__(self, start: Configuration, goal: Configuration):
        self.start = start  # The start configuration.
        self.goal = goal  # The end configuration.

    @classmethod
    def create_quarter_circle_problem(cls):
        start = Configuration(0, 0, 0.5*np.pi)
        goal = Configuration(9, 0, 0.5*np.pi)
        return cls(start, goal)

    @classmethod
    def load_from_file(cls, path: str):
        # reading file in one line format
        f = open(path, "r")
        list1 = [float(i) for i in f.readline().split(',')]
        start = Configuration(list1[0], list1[1], list1[2])
        goal = Configuration(list1[3], list1[4], list1[5])
        f.close()
        return cls(start, goal)

    def to_string(self):
        return f"Problem\tstart: {self.start.to_string()}\n\tgoal: {self.goal.to_string()}"
