import matplotlib.pyplot as plt

from MultiarcPath import *
from PathView import PathView
from Problem import Problem
from matplotlib.pyplot import *


def main():
    nums_appr = 100  # control the number of points by bezier approximation
    problem = Problem.create_quarter_circle_problem()


    '''
    plotting algorithms generated paths
    pathView.add has three argument: algorithm label, color and k for control point distance
    '''
    # plotting algorithm generated paths
    pathView = PathView(problem, nums_appr)
    pathView.add("bspline", "b", 1)
    pathView.add("bspline", "y", 0.8)
    pathView.add("bspline", "g", 0.6)
    pathView.add("bspline", "c", 0.4)
    pathView.add("bspline", "m", 0.2)
    pathView.add_arrow()
    pathView.show()


    '''
    plotting arc based paths
    pathView.add_multiarc has three argument: algorithm label, color and k for control point distance
    '''
    pathView = PathView(problem, nums_appr)
    pathView.add_multiarc("cubicspline", "b", 1)
    pathView.add_multiarc("cubicspline", "y", 0.8)
    pathView.add_multiarc("cubicspline", "g", 0.6)
    pathView.add_multiarc("cubicspline", "c", 0.4)
    pathView.add_multiarc("cubicspline", "m", 0.2)
    pathView.add_arrow()
    pathView.show()


    '''
    plotting curvature against path length
    pathView.add_curvature has three argument: algorithm label, color and k for control point distance
    '''
    pathView = PathView(problem, nums_appr)
    pathView.add_curvature("bezier", "-b", 1)
    pathView.add_curvature("bezier", "-y", 0.8)
    pathView.add_curvature("bezier", "-g", 0.6)
    pathView.add_curvature("bezier", "-c", 0.4)
    pathView.add_curvature("bezier", "-m", 0.2)
    pathView.show()


    '''
    calculating and compute the optimal value of k for given problem
    pathView.compute_strain has two argument: algorithm label, color
    '''
    pathView = PathView(problem, nums_appr)
    pathView.compute_strain("bezier", 'r')
    pathView.compute_strain("cubicspline", 'b')
    pathView.compute_strain("bspline", 'g')
    pathView.show()


if __name__ == '__main__':
    main()
