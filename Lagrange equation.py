import matplotlib.pyplot as plt
import numpy as np


def L(k, x, u):
    n = 1
    d = 1
    for i in range(len(x)):
        if i != k:
            n *= (u - x[i])
            d *= (x[k] - x[i])
    return n / d


def Lagrange(x, y, u):
    s = 0
    for i in range(len(x)):
        s += y[i] * L(i, x, u)
    return s


def plotLagrange(x, y, a, b):
    us = [j / 10 for j in range(a * 10, b * 10 + 1)]
    results = []
    for i in us:
        results.append(Lagrange(x, y, i))
    plt.plot(us, results, 'b-')


def fu(x):
    return 1 / (1 + 25 * x ** 2)


# first function

x1 = [-1, -0.5, 0]
y1 = [fu(i) for i in x1]
plotLagrange(x1, y1, -1, 0)
z1 = np.arange(-1, 0, 00.01)
plt.plot(z1, fu(z1))
plt.grid()
plt.show()

# second function

x2 = [0, 0.5, 1]
y2 = [fu(i) for i in x2]
plotLagrange(x2, y2, 0, 1)
z2 = np.arange(0, 1, 00.01)
plt.plot(z2, fu(z2))
plt.grid()
plt.show()
