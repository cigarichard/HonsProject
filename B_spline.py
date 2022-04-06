import numpy as np

from Problem import Problem


class B_spline:

    def __init__(self, problem: Problem, d: int, nums_approx: int):
        self.problem = problem
        self.n = 3  # number of vertex - 1
        self.k = 3  # power of the B-spline
        self.d = d  # ratio of distance for the vertex
        self.nums_approx = nums_approx
        self.knotVector = [0, 0, 0, 0, 1, 1, 1, 1]
        self.dist = self.problem.start.euclidean_dist(self.problem.goal)

    def add_control_point(self):
        # calculate the direction control points needed for B-spline
        k = self.d
        start_x = self.problem.start.x
        start_y = self.problem.start.y
        start_h = self.problem.start.h
        end_x = self.problem.goal.x
        end_y = self.problem.goal.y
        end_h = self.problem.goal.h
        x = [start_x, start_x + k * self.dist * np.cos(start_h), end_x - k * self.dist * np.cos(end_h), end_x]
        y = [start_y, start_y + k * self.dist * np.sin(start_h), end_y - k * self.dist * np.sin(end_h), end_y]
        return x, y

    def b_spline_basis(self, i, k, t, knotVector):
        if k == 0:  # if k=0, re-define the value
            if (knotVector[i] < t) & (t <= knotVector[i + 1]):  # if u between two knotVector, result will be 1
                # otherwise, is 0
                result = 1
            else:
                result = 0
        else:
            # calculate the length of local support
            length1 = knotVector[i + k] - knotVector[i]
            length2 = knotVector[i + k + 1] - knotVector[i + 1]
            # define the coefficient of the basis function
            if length1 == 0:
                alpha = 0
            else:
                alpha = (t - knotVector[i]) / length1
            if length2 == 0:
                beta = 0
            else:
                beta = (knotVector[i + k + 1] - t) / length2
            # recursion
            result = alpha * self.b_spline_basis(i, k - 1, t, knotVector) + beta * self.b_spline_basis(i + 1, k - 1, t,
                                                                                                       knotVector)
        return result

    def compute_curve(self):
        n = self.n
        k = self.k
        nums_approx = self.nums_approx + 1
        knotVector = self.knotVector
        x, y = self.add_control_point()
        basis_i = np.zeros((nums_approx,2))  # store the value of the basis function
        r = np.zeros((nums_approx,2))
        for i in range(n + 1):  # calculate the value of ith basis function of B-spline
            T = np.linspace(knotVector[k], knotVector[n + 1], nums_approx)  # take t=0.01 between each knotVector
            j = 0
            for t in T:
                knotVector = np.array(knotVector)
                basis_i[j] = self.b_spline_basis(i, k, t, knotVector)  # calculate the value of basis function
                j = j + 1
            r += [x[i], y[i]] * basis_i
        return r

