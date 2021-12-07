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
        h = arc_start_cfg.h + 0.85 * prop[i] * arc.phi

        if np.cos(h) == 1 or np.sin(h) == 1:
            y += 0
            x += 0
        else:
            x += split_arc * np.cos(h)
            y += split_arc * np.sin(h)
    return Configuration(x,y,h)

    # x = arc_start_cfg.x
    # y = arc_start_cfg.y
    # h = arc_start_cfg.h
    # cos_h = np.cos(h)
    # sin_h = np.sin(h)
    # if arc.is_straight():
    #     return Configuration(
    #         x + arc.arc_length * cos_h,
    #         y + arc.arc_length * sin_h,
    #         h
    #     )
    #
    # # The changes in x and y along the axes of the robot's local coordinate system.
    # dx = arc.radius * np.sin(arc.phi)
    # dy = arc.radius * (1 - np.cos(arc.phi))
    #
    # # Rotate the relative positions anti-clockwise by the angle of the robot's heading.
    # # This gives an absolute rather than a relative displacement in X-Y.
    # # By adding the current X and Y positions we get the new absolute position.
    # # To get the new heading, simply add the turn of the arc to the current heading.
    # return Configuration(
    #     x + dx * cos_h - dy * sin_h,
    #     y + dx * sin_h + dy * cos_h,
    #     angle_into_0_2pi(arc_start_cfg.h + arc.phi)
    # )


def angle_into_0_2pi(angle: float) -> float:
    return angle % (2 * np.pi)


# def compute_arc_plot(arc_start_cfg: Configuration, arc: Arc):
#     k = 0.1
#     split_arc = arc.arc_length / 10
#     prop = np.arange(0, 1, k)
#     x = arc_start_cfg.x
#     y = arc_start_cfg.y
#     x_plot = [x]
#     y_plot = [y]
#     for i in range(10):
#         h = arc_start_cfg.h + prop[i] * arc.phi
#         if np.cos(h) == 1 or np.sin(h) == 1:
#             y += 0
#             x += 0
#             x_plot.append(x)
#             y_plot.append(y)
#         else:
#             x += split_arc * np.cos(h)
#             y += split_arc * np.sin(h)
#             x_plot.append(x)
#             y_plot.append(y)
#     return Configuration(x, y, h), x_plot, y_plot


class MultiarcPath:
    def __init__(self, problem: Problem, arcs: List[Arc]):
        self.problem = Problem
        self.arcs = arcs

    def toString(self):
        return "this is a multiarc path"
