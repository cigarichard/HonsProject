from matplotlib import pyplot as plt

from Bezier import Bezier
from Curvature import Curvature
from MultiarcPath import *
from Problem import *


class PathView:
    # Crete a graphical user interface to display the paths.

    def __init__(self, problem: Problem):
        fig, ax = plt.subplots()
        self.problem = problem
        self.ax = ax
        self.bezier = Bezier(problem, 1, 1)

    def compute_bezier(self):
        # generate the points of bezier curve
        curve_points = self.bezier.get_curve()
        return curve_points

    def compute_multiarcPath(self):
        # generate the arc end configuration of each arc, and append its x and y coordinates into a list
        curve_points = self.compute_bezier()
        curvature = Curvature(curve_points, 100)
        arc_list = curvature.get_arc()
        multarcpath1 = self.problem.start
        x = [self.problem.start.x]
        y = [self.problem.start.y]
        for i in range(len(arc_list)):
            multarcpath1 = compute_arc_end_cfg(multarcpath1, arc_list[i])
            x.append(multarcpath1.x)
            y.append(multarcpath1.y)
        return x, y

    def compute_curvature(self, curve_points: List):
        # generate the curvature of the curve with corresponding length of curve
        curvature = Curvature(curve_points, 100)
        cur_curvature = curvature.cal_curvature()
        cur_split = curvature.split_cur()
        return cur_curvature, cur_split

    def generate_start_arrow(self):
        x = self.problem.start.x
        y = self.problem.start.y
        h = self.problem.start.h
        arr = ([x + 0.5 * np.cos(h), y + 0.5 * np.sin(h)])
        return np.array(arr)

    def generate_end_arrow(self):
        x = self.problem.goal.x
        y = self.problem.goal.y
        h = self.problem.goal.h
        arr = ([x + 0.5 * np.cos(h), y + 0.5 * np.sin(h)])
        return np.array(arr)

    def add_arrow(self):
        arr_start = self.generate_start_arrow()
        arr_end = self.generate_end_arrow()
        plt.annotate("", xy=(arr_start[0], arr_start[1]), xytext=(self.problem.start.x, self.problem.start.y),
                     arrowprops=dict(arrowstyle="->", color="coral"), label="direction")
        plt.annotate("", xy=(arr_end[0], arr_end[1]), xytext=(self.problem.goal.x, self.problem.goal.y),
                     arrowprops=dict(arrowstyle="->", color="coral"), label="direction")
        print(arr_end[0],arr_end[1])

    def add(self, label: str, color: str):
        # plot the path by different methods used
        # It takes two arguments, label: the name of the path, color: the color of the path on the graph
        if label == "bezierPath":
            curve_points = self.compute_bezier()
            x = curve_points[:, 0]
            y = curve_points[:, 1]
        if label == "multiarcPath":
            x, y = self.compute_multiarcPath()
        self.ax.plot(x, y, color, label=label)
        plt.xlabel("x")
        plt.ylabel("y")

    def add_control_points(self):
        control_points = self.bezier.add_control_point()
        plt.plot(control_points[:,0], control_points[:,1], "xb")

    def add_curvature(self, label: str, color: str):
        # plot the curvature of the path
        if label == "bezierPath":
            curve_points = self.compute_bezier()
            cur_curvature, cur_split = self.compute_curvature(curve_points)
        self.ax.plot(cur_split, cur_curvature[:], color, label=label)
        plt.xlabel("line length[m]")
        plt.ylabel("curvature [1/m]")

    def show(self):
        plt.grid(True)
        plt.legend()
        plt.show()
