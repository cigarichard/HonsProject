import numpy as np

from Configuration import Configuration
from CubicSpline import CubicSpline
from Problem import Problem


class CubicSpline2D:
    """
    2D Cubic Spline class
    """

    def __init__(self, problem: Problem, d: int):
        self.problem = problem
        self.start = self.problem.start
        self.goal = self.problem.goal
        self.d = d  # # ratio of distance for the vertex to compute the control points
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)
        self.x, self.y = self.add_control_point()
        self.s = self.__calc_s(self.x, self.y)
        self.sx = CubicSpline(self.s, self.x)
        self.sy = CubicSpline(self.s, self.y)

    def add_control_point(self):
        # calculate the direction control points needed for B-spline
        k = 0.9 * self.d
        start_x, start_y, start_h = self.start.x, self.start.y, self.start.h
        end_x, end_y, end_h = self.goal.x, self.goal.y, self.goal.h
        x, y, rx, ry = [], [], [], []
        x.append(start_x)
        y.append(start_y)
        rx.append(end_x)
        ry.append(end_y)
        start_1 = Configuration(start_x + 0.2 * k * self.dist * np.cos(start_h),
                                start_y + 0.2 * k * self.dist * np.sin(start_h), start_h)
        end_1 = Configuration(end_x - 0.2 * k * self.dist * np.cos(end_h), end_y - 0.2 * k * self.dist * np.sin(end_h),
                              end_h)
        theta = np.abs(start_h - end_h)
        start_r, end_r = start_1, end_1
        theta = np.abs(start_1.h - end_1.h)
        x.append(start_1.x)
        y.append(start_1.y)
        rx.append(end_1.x)
        ry.append(end_1.y)
        a = 0
        while a<2:
            start_r, end_r = self.conr_renew(start_r, end_r, self.dist, k, theta)
            x.append(start_r.x)
            y.append(start_r.y)
            rx.append(end_r.x)
            ry.append(end_r.y)
            a += 1

        rx.reverse()
        ry.reverse()
        for i in range(len(rx)):
            x.append(rx[i])
            y.append(ry[i])

        return x, y

    def conr_renew(self, start:Configuration, end:Configuration, dist, k, theta):

        start_2 = Configuration(start.x + 0.2 * k * self.dist * np.cos(start.h - (0.4 * theta)),
                                start.y + 0.2 * k * self.dist * np.sin(start.h - (0.4 * theta)),
                                start.h - 0.4 * theta)
        end_2 = Configuration(end.x - 0.2 * k * self.dist * np.cos(end.h - (0.4 * theta)),
                              end.y - 0.2 * k * self.dist * np.sin(end.h - (0.4 * theta)),
                              end.h - 0.4 * theta)
        return start_2, end_2

    def __calc_s(self, x, y):
        dx = np.diff(x)
        dy = np.diff(y)
        self.ds = np.hypot(dx, dy)
        s = [0]
        s.extend(np.cumsum(self.ds))
        return s

    def calc_position(self, s):  # to calculate the coordinate of each point on the curve
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
        return np.array(point)
