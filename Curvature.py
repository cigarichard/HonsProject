from typing import List
import numpy as np
from Arc import Arc


def euclidean_dist(p_1, p_2):
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    dist = np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dist


class Curvature:

    def __init__(self, curve_point: List, num_approx: int):
        self.curve_point = curve_point
        self.num_approx = num_approx  # control the numbers of split of the curve.

    def cal_curvature(self):
        # calculate the curvature of a curve

        dx_dt = np.gradient(self.curve_point[:, 0])
        dy_dt = np.gradient(self.curve_point[:, 1])
        d2x_dt2 = np.gradient(dx_dt)
        d2y_dt2 = np.gradient(dy_dt)
        curvature = (d2y_dt2 * dx_dt - d2x_dt2 * dy_dt) / (dx_dt * dx_dt + dy_dt * dy_dt) ** 1.5
        # print("length of curvature", len(curvature))
        return curvature

    def curve_len(self):
        # calculate the total length of the curve
        curve_len = 0
        for i in range(len(self.curve_point) - 1):
            curve_len += euclidean_dist(self.curve_point[i], self.curve_point[i + 1])
        # print("curve length", curve_len)
        return curve_len

    def split_cur(self):
        # split a curve into k pieces and use split against curvature
        k = len(self.curve_point)
        curve_len = self.curve_len()
        split = np.linspace(0, curve_len, num=(k))
        return split

    def arc_len(self):
        """
        :return: split a curve path into n arcs
        """
        arc_len = []
        sum = 0
        for i in range(len(self.curve_point) - 1):
            arc_len.append(euclidean_dist(self.curve_point[i], self.curve_point[i + 1]))
            sum += euclidean_dist(self.curve_point[i], self.curve_point[i + 1])
        # print("total of arc length ", sum)
        # print("numbers of arc", len(arc_len))
        return np.array(arc_len)

    def get_curvature_mean(self):
        # by taking numbers of arc, calculate the curvature of each arc
        curvature = self.cal_curvature()
        # print(curvature)
        curvature_mean = []
        for i in range(len(curvature)-1):
            curvature_mean.append((np.sum(curvature[i: (i + 2)])) / 2 )
        # print("numbers of curvature mean", len(curvature_mean))
        return np.array(curvature_mean)

    def get_arc(self) -> List[Arc]:
        # add all the arc into a list
        k = len(self.curve_point)-1
        # k = self.num_approx
        print(k)
        arc_len = self.arc_len()
        curvature = self.get_curvature_mean()
        arc_list = []
        for i in range(k):
            arc_list.append(Arc(curvature[i], arc_len[i]))
        return arc_list
