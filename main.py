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
    bezier = Bezier(problem,1)
    curve1 = bezier.get_curve()
    curvature = Curvature(curve1, 100)
    curve1_len = curvature.curve_len()
    print(curve1_len)
    cur_curvature = curvature.cul_curvature()

    cur_split = curvature.split_cur()
    arc_list = curvature.get_arc()
    multarcpath1 = problem.start
    for i in range(len(arc_list)):
        multarcpath1 = compute_arc_end_cfg(multarcpath1, arc_list[i])
        print(multarcpath1.to_string())


    '''
    plot
    '''
    # plt.subplots(1)
    # start1 = problem.start
    # for i in range(len(arc_list)):
    #     start1, x_plot, y_plot = compute_arc_plot(start1, arc_list[i])
    #     plt.plot(x_plot, y_plot, "-r")
    #     # plt.plot(multarcpath1.x, multarcpath1.y, "xb")
    # plt.grid(True)
    # plt.legend()
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()
    #
    # # list_arc = bezier.approx_with_arc(2)
    # # multarcpath1 = problem.start
    # # plt.subplots(1)
    # # for i in range(len(list_arc)):
    # #     multarcpath1, x_plot, y_plot = compute_arc_end_cfg(multarcpath1, list_arc[i])
    # #     print(multarcpath1.to_string())
    # #     plt.plot(x_plot, y_plot, "-r")
    # # plt.grid(True)
    # # plt.legend()
    # # plt.xlabel("x")
    # # plt.ylabel("y")
    # # plt.show()
    #
    # plt.subplots(1)
    # plt.plot(curve1[:, 0], curve1[:, 1])
    # plt.grid(True)
    # plt.legend()
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()
    #
    # plt.subplots(1)
    # plt.plot(cur_split, cur_curvature[:], "-r", label="curvature1")
    # plt.grid(True)
    # plt.legend()
    # plt.xlabel("line length[m]")
    # plt.ylabel("curvature [1/m]")
    # plt.show()

    pathView = PathView(problem)
    pathView.add(curve1, "b")
    pathView.add(curve1, "xb")
    plt.show()


if __name__ == '__main__':
    main()
