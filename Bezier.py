import numpy as np
from Problem import Problem


class Bezier:
    def __init__(self, problem: Problem, k: float, num_approx: int):
        self.problem = problem
        self.k = k  # k is the distance controller of adding control points
        self.num_approx = num_approx  # number of points generated by bezier approximation
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)

    def add_control_point(self):
        # calculate the direction control points needed for Bézier curve
        k = self.k
        start_x = self.problem.start.x
        start_y = self.problem.start.y
        start_h = self.problem.start.h
        end_x = self.problem.goal.x
        end_y = self.problem.goal.y
        end_h = self.problem.goal.h
        dir_con = [[start_x, start_y],
                   [start_x + k * self.dist * np.cos(start_h), start_y + k * self.dist * np.sin(start_h)],
                   [end_x - k * self.dist * np.cos(end_h), end_y - k * self.dist * np.sin(end_h)], [end_x, end_y]]
        return np.array(dir_con)

    def get_point(self, t, points):
        while len(points) > 1:
            newpoints = []
            for p in range(0, len(points) - 1):
                newpoints += [(1 - t) * points[p] + t * points[p + 1]]
            points = newpoints
        return points

    def compute_curve(self):
        # generate the points of bezier curve
        k = 1 / self.num_approx
        points = self.add_control_point()
        tlist = np.arange(0, 1 + k, k)
        curve_point = self.get_point(tlist[0], points)
        for t in tlist[1:]:
            curve_point += self.get_point(t, points)
        return np.array(curve_point)
