from typing import List
import numpy as np
import Problem
from Arc import Arc
from Configuration import Configuration
from Problem import Problem


def compute_arc_end_cfg(arc_start_cfg: Configuration, arc: Arc) -> Configuration:
    x = arc_start_cfg.x
    y = arc_start_cfg.y
    h = arc_start_cfg.h
    cos_h = np.cos(h)
    sin_h = np.sin(h)
    if arc.is_straight():
        return Configuration(
            x + arc.arc_length * cos_h,
            y + arc.arc_length * sin_h,
            h
        )

    # The changes in x and y along the axes of the robot's local coordinate system.
    dx = arc.radius * np.sin(arc.phi)
    dy = arc.radius * (1 - np.cos(arc.phi))
    # Rotate the relative positions anti-clockwise by the angle of the robot's heading.
    # This gives an absolute rather than a relative displacement in X-Y.
    # By adding the current X and Y positions we get the new absolute position.
    # To get the new heading, simply add the turn of the arc to the current heading.
    return Configuration(
        x + dx * cos_h - dy * sin_h,
        y + dx * sin_h + dy * cos_h,
        angle_into_0_2pi(arc_start_cfg.h + arc.phi)
    )


def angle_into_0_2pi(angle: float) -> float:
    return angle % (2 * np.pi)


class MultiarcPath:
    def __init__(self, problem: Problem, arcs: List[Arc]):
        self.problem = Problem
        self.arcs = arcs

    def toString(self):
        return "this is a multiarc path"
