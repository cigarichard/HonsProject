from typing import List

from matplotlib import pyplot as plt

from Bezier import Bezier
from Problem import *


class PathView:
    # Crete a graphical user interface to display the paths.

    def __init__(self, problem: Problem):
        fig, ax = plt.subplots()
        self.problem = problem
        self.ax = ax

    def add(self, curve_points: List, color: str):
        self.ax.plot(curve_points[:, 0], curve_points[:, 1], color)
