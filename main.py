import matplotlib.pyplot as plt

from MultiarcPath import *
from PathView import PathView
from Problem import Problem
from matplotlib.pyplot import *


def main():
    nums_appr = 100  # control the number of points by bezier approximation
    problem = Problem.create_quarter_circle_problem()


    '''
    plot
    '''
    pathView = PathView(problem, nums_appr)
    # pathView.add("bezier", "b", 0.4)
    # pathView.add("bezier", "y", 0.8)
    # pathView.add("bezier", "g", 0.6)
    # pathView.add("bezier", "c", 0.4)
    # pathView.add("bezier", "m", 0.2)
    pathView.add("bspline", "b", 1)
    pathView.add("bspline", "y", 0.8)
    pathView.add("bspline", "g", 0.6)
    pathView.add("bspline", "c", 0.4)
    pathView.add("bspline", "m", 0.2)
    # pathView.add("cubicspline", "c", 0.4)
    # pathView.add("cubicspline", "y", 0.8)
    # pathView.add("cubicspline", "g", 0.6)
    # pathView.add("cubicspline", "c", 0.4)
    # pathView.add("cubicspline", "m", 0.2)
    # print("done")
    pathView.add_arrow()
    pathView.show()

    # pathView = PathView(problem, nums_appr)
    # # pathView.add("bezier", "b", 0.4)
    # # pathView.add_multiarc("bezier", "r", 0.4)
    # # pathView.add("cubicspline", "y", 0.4)
    # # pathView.add_multiarc("cubicspline", "g", 0.4)
    # # pathView.add_multiarc("bspline", "b", 1)
    # # pathView.add_multiarc("bspline", "y", 0.8)
    # # pathView.add_multiarc("bspline", "g", 0.6)
    # # pathView.add_multiarc("bspline", "c", 0.4)
    # # pathView.add_multiarc("bspline", "m", 0.2)
    # pathView.add_multiarc("cubicspline", "b", 1)
    # pathView.add_multiarc("cubicspline", "y", 0.8)
    # pathView.add_multiarc("cubicspline", "g", 0.6)
    # pathView.add_multiarc("cubicspline", "c", 0.4)
    # pathView.add_multiarc("cubicspline", "m", 0.2)
    # pathView.add_arrow()
    # pathView.show()
    #
    # pathView = PathView(problem, nums_appr)
    # pathView.add_curvature("bezier", "-b", 1)
    # pathView.add_curvature("bezier", "-y", 0.8)
    # pathView.add_curvature("bezier", "-g", 0.6)
    # pathView.add_curvature("bezier", "-c", 0.4)
    # pathView.add_curvature("bezier", "-m", 0.2)
    # # pathView.add_curvature("bspline", "b", 1)
    # # pathView.add_curvature("bspline", "y", 0.8)
    # # pathView.add_curvature("bspline", "g", 0.6)
    # # pathView.add_curvature("bspline", "c", 0.4)
    # # pathView.add_curvature("bspline", "m", 0.2)
    # # pathView.add_curvature("cubicspline", "c", 0.4)
    # # pathView.add_curvature("cubicspline", "y", 0.8)
    # # pathView.add_curvature("cubicspline", "g", 0.6)
    # # pathView.add_curvature("cubicspline", "c", 0.4)
    # # pathView.add_curvature("cubicspline", "m", 0.2)
    # pathView.show()

    pathView = PathView(problem, nums_appr)
    pathView.compute_strain("bezier", 'r')
    pathView.compute_strain("cubicspline", 'b')
    pathView.compute_strain("bspline", 'g')
    pathView.show()


if __name__ == '__main__':
    main()
