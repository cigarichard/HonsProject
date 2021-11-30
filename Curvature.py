from typing import List

import numpy as np

from Arc import Arc


def euclidean_dist(p_1, p_2):
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    dist = np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dist


class Curvature:

    def __init__(self, curve_point: List, k: int):
        self.curve_point = curve_point
        self.k = k

    def cul_curvature(self):
        dx_dt = np.gradient(self.curve_point[:, 0])
        dy_dt = np.gradient(self.curve_point[:, 1])
        d2x_dt2 = np.gradient(dx_dt)
        d2y_dt2 = np.gradient(dy_dt)
        curvature = (d2y_dt2 * dy_dt - d2x_dt2 * dy_dt) / (dx_dt * dx_dt + dy_dt * dy_dt) ** 1.5
        return curvature

    def curve_len(self):
        """
        :return: the length of the curve
        """
        curve_len = 0
        for i in range(len(self.curve_point) - 1):
            curve_len += euclidean_dist(self.curve_point[i], self.curve_point[i + 1])
        return curve_len

    def split_cur(self):
        curve_len = self.curve_len()
        split = np.linspace(0, curve_len, num=101)
        return split

    def arc_len(self):
        """
        :return: split a curve path into n arcs
        """
        k = self.k
        cur_len = self.curve_len()
        arc_len = []
        for i in range(k):
            arc_len.append(cur_len / k)
        return np.array(arc_len)

    def get_curvature_mean(self):
        curvature = self.cul_curvature()
        k = self.k
        l = len(curvature) // self.k
        curvature_mean = []
        for i in range(k):
            curvature_mean.append((np.sum(curvature[(i * l): (i + 1) * l])) / l)
        return np.array(curvature_mean)

    def get_arc(self) -> List[Arc]:
        k = self.k
        arc_len = self.arc_len()
        curvature = self.get_curvature_mean()
        arc_list = []
        for i in range(k):
            arc_list.append(Arc(curvature[i], arc_len[i]))
        return arc_list
