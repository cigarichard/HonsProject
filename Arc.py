import numpy as np
import Configuration


class Arc:

    def __init__(self, curvature: float, arc_length: float):
        self.curvature = curvature  # The curvature of each arc
        self.arc_length = arc_length  # The length of arcs
        self.radius = 1 / self.curvature
        self.phi = self.arc_length * self.curvature

    def is_straight(self):
        return self.curvature == 0

    def strain(self):
        return self.curvature ** 2 * self.arc_length

    def to_string(self):
        return f"Arc(arc_length = {self.arc_length}, curvature = {self.curvature}, phi = {self.phi})"
