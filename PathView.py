from matplotlib import pyplot as plt

from B_spline import B_spline
from Bezier import Bezier
from CubicSpline2D import CubicSpline2D
from Curvature import Curvature
from MultiarcPath import *
from CubicSpline import *


class PathView:
    # Crete a graphical user interface to display the paths.

    def __init__(self, problem: Problem, num_approx: int):
        fig, ax = plt.subplots()
        self.problem = problem
        self.ax = ax
        self.num_approx = num_approx
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)

    def add_multiarc(self, label, color, k):
        # generate the arc end configuration of each arc, and append its x and y coordinates into a list
        if label == "bezier":
            bezier = Bezier(self.problem, k, self.num_approx)
            curve_points = bezier.compute_curve()
        if label == "bspline":
            bspline = B_spline(self.problem, k, self.num_approx)
            curve_points = bspline.compute_curve()
        if label == "cubicspline":
            cubicspline = CubicSpline2D(self.problem, k)
            curve_points = cubicspline.compute_curve()
        curvature = Curvature(curve_points, self.num_approx)
        arc_list = curvature.get_arc()
        multarcpath = self.problem.start
        strain = 0
        x = [self.problem.start.x]
        y = [self.problem.start.y]
        for i in range(len(arc_list)):
            multarcpath = compute_arc_end_cfg(multarcpath, arc_list[i])
            strain += arc_list[i].strain()
            x.append(multarcpath.x)
            y.append(multarcpath.y)
        print("strain = ", strain)
        self.ax.plot(x, y, color, label="multiarc" + label + "@" + str(k))

    def compute_curvature(self, curve_points: List):
        # generate the curvature of the curve with corresponding length of curve
        curvature = Curvature(curve_points, self.num_approx)
        cur_curvature = curvature.cal_curvature()
        cur_split = curvature.split_cur()
        return cur_split, cur_curvature

    def generate_start_arrow(self):
        dist = self.dist
        x = self.problem.start.x
        y = self.problem.start.y
        h = self.problem.start.h
        arr = ([x + 0.3 * dist * np.cos(h), y + 0.3 * dist * np.sin(h)])
        return np.array(arr)

    def generate_end_arrow(self):
        dist = self.dist
        x = self.problem.goal.x
        y = self.problem.goal.y
        h = self.problem.goal.h
        arr = ([x - 0.3 * dist * np.cos(h), y - 0.3 * dist * np.sin(h)])
        return np.array(arr)

    def add_arrow(self):
        arr_start = self.generate_start_arrow()
        arr_end = self.generate_end_arrow()
        plt.annotate("", xy=(arr_start[0], arr_start[1]), xytext=(self.problem.start.x, self.problem.start.y),
                     arrowprops=dict(arrowstyle="->", color="gold"), label="direction")
        plt.annotate("", xy=(self.problem.goal.x, self.problem.goal.y), xytext=(arr_end[0], arr_end[1]),
                     arrowprops=dict(arrowstyle="->", color="gold"), label="direction")

    def add(self, label: str, color: str, k: float):
        # plot the path by different methods used
        # It takes three arguments, label: the name of the path, color: the color of the path on the graph
        # k: control the distance of different control point to generated different path

        if label == "bezier":
            bezier = Bezier(self.problem, k, self.num_approx)
            curve_points = bezier.compute_curve()
            control_points = bezier.add_control_point()
            x = curve_points[:, 0]
            y = curve_points[:, 1]
            self.ax.plot(control_points[1:-1][:, 0], control_points[1:-1][:, 1], "x" + color)
        if label == "bspline":
            bspline = B_spline(self.problem, k, self.num_approx)
            curve_points = bspline.compute_curve()
            rx, ry = bspline.add_control_point()
            x = curve_points[:, 0]
            y = curve_points[:, 1]
            self.ax.plot(rx[1:-1], ry[1:-1], "x" + color)
        if label == "cubicspline":
            cubicspline = self.cubicspline.compute_curve()
            x = cubicspline[:, 0]
            y = cubicspline[:, 1]
        self.ax.plot(x, y, color, label=label + "@" + str(k))
        self.ax.plot(self.problem.start.x, self.problem.start.y, "xk")
        self.ax.plot(self.problem.goal.x, self.problem.goal.y, "xk")
        plt.xlabel("x")
        plt.ylabel("y")

    def add_curvature(self, label: str, color: str, k: float):
        # plot the curvature of the path
        if label == "bezier":
            bezier = Bezier(self.problem, k, self.num_approx)
            bezierPoints = bezier.compute_curve()
            cur_split, cur_curvature = self.compute_curvature(bezierPoints)
            # print(len(cur_split), len(cur_curvature))
        if label == "bspline":
            bspline = B_spline(self.problem, k, self.num_approx)
            bsplinePoints = bspline.compute_curve()
            cur_split, cur_curvature = self.compute_curvature(bsplinePoints)
            # print(len(cur_split), len(cur_curvature))
        if label == "cubicspline":
            cubicspline = self.cubicspline.compute_curve()
            cur_split, cur_curvature = self.compute_curvature(cubicspline)
            # print(len(cur_split), len(cur_curvature))
        self.ax.plot(cur_split, cur_curvature[:], color, label=label + "@" + str(k))
        plt.xlabel("path length[m]")
        plt.ylabel("curvature [1/m]")

    def show(self):
        plt.grid(True)
        plt.legend()
        plt.show()
