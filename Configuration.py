import numpy as np


class Configuration:
    def __init__(self, x: float, y: float, h: float):
        self.x = x  # The x-coordinate.
        self.y = y  # The y-coordinate.
        self.h = h  # The heading angle i.e. orientation.

    def to_string(self):
        return f"Cfg(x = {self.x}, y = {self.y}, h = {self.h})"

    def euclidean_dist(self, other):
        # calculate the euclidean distance
        x_1 = self.x
        y_1 = self.y
        x_2 = other.x
        y_2 = other.y
        return np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)