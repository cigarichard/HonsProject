import Bezier
import MultiarcPath
from Bezier import *
from Curvature import *
from MultiarcPath import *
from PathView import PathView
from Problem import Problem
from CubicSpline import *
import matplotlib.pyplot as plt


def main():
    nums_appr = 100  # control the number of points by bezier approximation
    dist_con = 0.2  # control the distance of direction control points in bezier approximation
    problem = Problem.create_quarter_circle_problem()
    bezier = Bezier(problem, dist_con, nums_appr)
    '''
    plot
    '''
    pathView = PathView(problem, nums_appr, dist_con)
    pathView.add("bezierPath", "b")
    pathView.add("multiarcPath", "r")
    pathView.add("bspline", "g")
    pathView.add("cubicspline", "y")
    pathView.add_control_points()
    pathView.add_arrow()
    pathView.show()

    pathView = PathView(problem, nums_appr, dist_con)
    pathView.add_curvature("bezierPath", "-b")
    pathView.add_curvature("bspline", "r")
    # pathView.add_curvature("cubicspline", "y")
    pathView.show()


if __name__ == '__main__':
    main()
