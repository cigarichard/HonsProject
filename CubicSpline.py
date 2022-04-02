import numpy as np
import bisect


class CubicSpline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b, self.c, self.d = [], [], []
        self.nx = len(x)  # dimension of x
        h = np.diff(x) # to calculate h = the difference between each x value

        # calculate coefficient a
        self.a = [iy for iy in y]

        # calculate coefficient c
        A = self.__calc_A(h)
        B = self.__calc_B(h)
        self.c = np.linalg.solve(A, B)

        # calculate spline coefficient b and d
        for i in range(self.nx - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * h[i]))
            tb = (self.a[i + 1] - self.a[i]) / h[i] - h[i] * \
                 (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            self.b.append(tb)

    def __calc_A(self, h): # calculate matrix A
        A = np.zeros((self.nx, self.nx))
        A[0, 0] = 1.0
        for i in range(self.nx - 1):
            if i != (self.nx - 2):
                A[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])
            A[i + 1, i] = h[i]
            A[i, i + 1] = h[i]

        A[0, 1] = 0.0
        A[self.nx - 1, self.nx - 2] = 0.0
        A[self.nx - 1, self.nx - 1] = 1.0
        return A

    def __calc_B(self, h): # calculate matrix B
        B = np.zeros(self.nx)
        for i in range(self.nx - 2):
            B[i + 1] = (3.0 * (self.a[i + 2] - self.a[i + 1]) / h[i + 1] - 3.0 * (self.a[i + 1] - self.a[i])) / h[i]
        return B

    def calc(self, t): # calculate the coordinates of each point on the curve
        i = bisect.bisect(self.x, t) - 1
        if i >= len(self.b):
            i -= 1
        # print(i, self.x, t)
        dx = t - self.x[i]
        result = self.a[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0
        return result
