from typing import List
import numpy as np
import Problem
from Arc import Arc
from Configuration import Configuration
from Problem import Problem


def compute_arc_end_cfg(arc_start_cfg: Configuration, arc: Arc) -> Configuration:
    k = 0.01
    split_arc = arc.arc_length / 100
    prop = np.arange(0, 1 + k, k)
    x = arc_start_cfg.x
    y = arc_start_cfg.y
    x_plot = [x]
    y_plot = [y]
    for i in range(101):
        h = arc_start_cfg.h + prop[i] * arc.phi
        # x += split_arc * np.cos(h)
        # x_plot.append(x)
        # y += split_arc * np.sin(h)
        # y_plot.append(y)
        if np.cos(h) == 1:
            x += 0
        else:
            x += split_arc * np.cos(h)
        x_plot.append(x)
        if np.sin(h) == 1:
            y += 0
        else:
            y += split_arc * np.sin(h)
        y_plot.append(y)
    return Configuration(x, y, h), x_plot, y_plot


class MultiarcPath:
    def __init__(self, problem: Problem, arcs: List[Arc]):
        self.problem = Problem
        self.arcs = arcs

    def toString(self):
        return "this is a multiarc path"
