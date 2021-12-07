import Bezier
import MultiarcPath
from Bezier import *
from Curvature import *
from MultiarcPath import *
from PathView import PathView
from Problem import Problem
import matplotlib.pyplot as plt


def main():
    problem = Problem.create_quarter_circle_problem()
    bezier = Bezier(problem, 1, 1)
    curve1 = bezier.get_curve()
    curvature = Curvature(curve1, 100)
    curve1_len = curvature.curve_len()
    print(curve1_len)

    arc_list = curvature.get_arc()
    multarcpath1 = problem.start
    for i in range(len(arc_list)):
        multarcpath1 = compute_arc_end_cfg(multarcpath1, arc_list[i])
        # print(multarcpath1.to_string())

    '''
    plot
    '''
    pathView = PathView(problem)
    pathView.add("bezierPath", "b")
    pathView.add("multiarcPath", "r")
    pathView.add_control_points()
    pathView.add_arrow()
    pathView.show()

    pathView = PathView(problem)
    pathView.add_curvature("bezierPath", "-b")
    pathView.show()


if __name__ == '__main__':
    main()
