import numpy as np


def inv(x):
    x = np.array(x)
    n = x.shape[0]
    a = np.c_[x, np.identity(n)]
    for i in range(n):
        if a[i, i] == 0:
            index = np.where(abs(a[i + 1:, i]) == max(abs(a[i + 1:, i])))
            a[i], a[i + index[0] + 1] = np.copy(a[i + index[0] + 1]), np.copy(a[i])
        if a[i, i] != 1:
            a[i] = a[i] / a[i, i]
        for j in range(n):
            if j != i:
                a[j] = a[j] - a[i] * (a[j, i] / a[i, i])
    return a[:, n:]
