from typing import List
import numpy as np
import Problem
from Arc import Arc
from Configuration import Configuration
from Problem import Problem


def compute_arc_end_cfg(arc_start_cfg: Configuration, arc: Arc) -> Configuration:
    k = 0.1
    split_arc = arc.arc_length / 10
    prop = np.arange(0, 1, k)
    x = arc_start_cfg.x
    y = arc_start_cfg.y
    for i in range(10):
        h = arc_start_cfg.h + prop[i] * arc.phi

        if np.cos(h) == 1 or np.sin(h) == 1:
            y += 0
            x += 0
        else:
            x += split_arc * np.cos(h)
            y += split_arc * np.sin(h)
        # if arc.phi > 0:
        #     x += split_arc * np.cos(h)
        # else:
        #     x += split_arc * np.cos(h)

        # if arc.phi > 0:
        #     y += split_arc * np.sin(h)
        # else:
        #     y += split_arc * np.sin(h)
    # if y > 0.2 or y < 0.8:
    #     print(arc_start_cfg.h, h, arc.phi)

    return Configuration(x, y, h)


def compute_arc_plot(arc_start_cfg: Configuration, arc: Arc):
    k = 0.1
    split_arc = arc.arc_length / 10
    prop = np.arange(0, 1, k)
    x = arc_start_cfg.x
    y = arc_start_cfg.y
    x_plot = [x]
    y_plot = [y]
    for i in range(10):
        h = arc_start_cfg.h + prop[i] * arc.phi
        if np.cos(h) == 1 or np.sin(h) == 1:
            y += 0
            x += 0
            x_plot.append(x)
            y_plot.append(y)
        else:
            x += split_arc * np.cos(h)
            y += split_arc * np.sin(h)
            x_plot.append(x)
            y_plot.append(y)
    return Configuration(x, y, h), x_plot, y_plot


class MultiarcPath:
    def __init__(self, problem: Problem, arcs: List[Arc]):
        self.problem = Problem
        self.arcs = arcs

    def toString(self):
        return "this is a multiarc path"
