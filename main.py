import Bezier
import MultiarcPath
from Bezier import *
from Curvature import *
from MultiarcPath import *
from PathView import PathView
from Problem import Problem
import matplotlib.pyplot as plt


def main():
    nums_appr = 100  # control the number of points by bezier approximation
    dist_con = 1  # control the distance of direction control points in bezier approximation
    problem = Problem.create_quarter_circle_problem()
    bezier = Bezier(problem, 1, dist_con, nums_appr)
    curve1 = bezier.get_curve()
    curvature = Curvature(curve1, nums_appr)

    arc_list = curvature.get_arc()
    multarcpath1 = problem.start
    for i in range(len(arc_list)):
        multarcpath1 = compute_arc_end_cfg(multarcpath1, arc_list[i])

    '''
    plot
    '''
    pathView = PathView(problem, nums_appr, dist_con)
    pathView.add("bezierPath", "b")
    pathView.add("multiarcPath", "r")
    pathView.add_control_points()
    pathView.add_arrow()
    pathView.show()

    pathView = PathView(problem, nums_appr, dist_con)
    pathView.add_curvature("bezierPath", "-b")
    pathView.show()


if __name__ == '__main__':
    main()
