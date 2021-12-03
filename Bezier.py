import math
from typing import List

import numpy as np

from Configuration import Configuration
from Arc import Arc
from Problem import Problem


class Bezier:
    def __init__(self, problem: Problem, nums_arc: int):
        self.problem = problem
        self.nums_arc = int

    @staticmethod
    def approx_with_arc(nums_arc: int) -> List[Arc]:
        arc1 = Arc(1 / 2 * math.pi, 1)
        arc2 = Arc(-1 / 2 * math.pi, 1)
        list_arc = [arc1, arc2]
        return list_arc

    def add_control_point(self):
        start_x = self.problem.start.x
        start_y = self.problem.start.y
        start_h = self.problem.start.h
        end_x = self.problem.goal.x
        end_y = self.problem.goal.y
        end_h = self.problem.goal.h
        dist = self.problem.start.euclidean_dist(self.problem.goal)
        dir_con = [[start_x, start_y], [start_x + dist * np.cos(start_h), start_y + dist * np.sin(start_h)],
                   [end_x - dist * np.cos(end_h), end_y - dist * np.sin(end_h)], [end_x, end_y]]
        return np.array(dir_con)

    def get_point(self, t, points):
        while len(points) > 1:
            newpoints = []
            for p in range(0, len(points) - 1):
                newpoints += [(1 - t) * points[p] + t * points[p + 1]]
            points = newpoints
        return points

    def get_curve(self):
        k = 0.01
        points = self.add_control_point()
        tlist = np.arange(0, 1+k, 0.01)
        curve_point = self.get_point(tlist[0], points)
        for t in tlist[1:]:
            curve_point += self.get_point(t, points)
        return np.array(curve_point)
