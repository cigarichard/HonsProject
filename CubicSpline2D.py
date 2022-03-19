import numpy as np

from CubicSpline import CubicSpline
from Problem import Problem


class CubicSpline2D:
    """
    2D Cubic Spline class
    """

    def __init__(self, problem: Problem, d: int):
        self.problem = problem
        self.d = d  # # ratio of distance for the vertex to compute the control points
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)
        self.x, self.y = self.add_control_point()
        self.s = self.__calc_s(self.x, self.y)
        self.sx = CubicSpline(self.s, self.x)
        self.sy = CubicSpline(self.s, self.y)

    def add_control_point(self):
        # calculate the direction control points needed for B-spline
        k = 0.5 * self.d
        start_x = self.problem.start.x
        start_y = self.problem.start.y
        start_h = self.problem.start.h
        end_x = self.problem.goal.x
        end_y = self.problem.goal.y
        end_h = self.problem.goal.h
        x = [start_x, start_x + k * self.dist * np.cos(start_h), end_x - k * self.dist * np.cos(end_h), end_x]
        y = [start_y, start_y + k * self.dist * np.sin(start_h), end_y - k * self.dist * np.sin(end_h), end_y]
        return x, y

    def __calc_s(self, x, y):
        dx = np.diff(x)
        dy = np.diff(y)
        self.ds = np.hypot(dx, dy)
        s = [0]
        s.extend(np.cumsum(self.ds))
        return s

    def calc_position(self, s): # to calculate the coordinate of each point on the curve
        x = self.sx.calc(s)
        y = self.sy.calc(s)
        return x, y

    def compute_curve(self):
        ds = self.s[-1] / 101  # distance of each interpolated points
        # and there will be 100 points generated to construct the curve
        s = np.arange(0, self.s[-1], ds)
        point = []
        for i_s in s:
            ix, iy = self.calc_position(i_s)
            point.append([ix, iy])
        print(len(point))
        return np.array(point)
