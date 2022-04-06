import numpy as np

from Configuration import Configuration
from CubicSpline import CubicSpline
from Problem import Problem


class CubicSpline2D:
    """
    2D Cubic Spline class
    """

    def __init__(self, problem: Problem, d: int, nums_approx: int):
        self.problem = problem
        self.start = self.problem.start
        self.goal = self.problem.goal
        self.d = d  # # ratio of distance for the vertex to compute the control points
        self.nums_approx = nums_approx
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)
        self.x, self.y = self.add_control_point()
        self.s = self.__calc_s(self.x, self.y)
        self.sx = CubicSpline(self.s, self.x)
        self.sy = CubicSpline(self.s, self.y)

    def add_control_point(self):
        # calculate the direction control points needed for B-spline
        k = 0.99 * self.d
        ks = 0.4
        start_1 = Configuration(self.start.x + ks * k * self.dist * np.cos(self.start.h),
                                self.start.y + ks * k * self.dist * np.sin(self.start.h),
                                self.start.h)
        end_1 = Configuration(self.goal.x - ks * k * self.dist * np.cos(self.goal.h),
                              self.goal.y - ks * k * self.dist * np.sin(self.goal.h),
                              self.goal.h)

        theta = (start_1.h - end_1.h)
        if theta != 0:
            start_2 = Configuration(start_1.x + ks * k * self.dist * np.cos(start_1.h + (0.5 * theta)),
                                    start_1.y + ks * k * self.dist * np.sin(start_1.h + (0.5 * theta)),
                                    start_1.h - 0.5 * theta)
            end_2 = Configuration(end_1.x - ks * k * self.dist * np.cos(end_1.h + (0.5 * theta)),
                                  end_1.y - ks * k * self.dist * np.sin(end_1.h + (0.5 * theta)),
                                  end_1.h + 0.5 * theta)
            x = [self.start.x, start_1.x, start_2.x, end_2.x, end_1.x, self.goal.x]
            y = [self.start.y, start_1.y, start_2.y, end_2.y, end_1.y, self.goal.y]
        else:
            theta = self.start.h
            start_2 = Configuration(start_1.x + ks * k * self.dist * np.cos(start_1.h - (0.5 * theta)),
                                    start_1.y + ks * k * self.dist * np.sin(start_1.h - (0.5 * theta)),
                                    start_1.h + 0.5 * theta)
            end_2 = Configuration(end_1.x - ks * k * self.dist * np.cos(end_1.h - (0.5 * theta)),
                                  end_1.y - ks * k * self.dist * np.sin(end_1.h - (0.5 * theta)),
                                  end_1.h - 0.5 * theta)
            mid = Configuration(self.goal.x / 2, self.goal.y / 2, self.goal.h / 2)
            x = [self.start.x, start_1.x, start_2.x, mid.x, end_2.x, end_1.x, self.goal.x]
            y = [self.start.y, start_1.y, start_2.y, mid.y, end_2.y, end_1.y, self.goal.y]
        return x, y

    def __calc_s(self, x, y):
        dx = np.diff(x)
        dy = np.diff(y)
        self.ds = np.hypot(dx, dy)
        # print(self.ds)
        s = [0]
        s.extend(np.cumsum(self.ds))
        # print("s:", s)
        return s


    def compute_curve(self): # to calculate the coordinate of each point on the curve
        ds = self.s[-1] / (self.nums_approx+1)  # distance of each interpolated points
        # and there will be 101 points generated to construct the curve
        s = np.arange(0, self.s[-1], ds)
        point = []
        for i_s in s:
            # print(i_s)
            ix = self.sx.calc(i_s)
            iy = self.sy.calc(i_s)
            point.append([ix, iy])
        return np.array(point)
