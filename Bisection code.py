import numpy as np
import matplotlib.pyplot as plt
import numpy as np

L = []


def f(x):
    return np.sqrt(x)


def bisection(a, b, t):
    p = (a + b) / 2
    while abs(a - b) >  t :
        p_old = p
        p = (a + b) / 2
        if f(p) * f(a) > 0 : 
            a = p
        else:
            b = p
        L.append([a, b, f(a), f(p), p, p_old])
    return p


solution = bisection (1,2,5e-8)
header = "{:9s}{:10s}{:10s}{:10s}{:10s}{:10s}{:10s}".format('It#', 'a', 'b', 'p', 'f(a)', 'f(p)', 'abs(pn - pn-1)/ pn')
print(header)
print('_' * len(header))
count = 1
for _ in L:
    print("{:4d}{:10.6f}{:10.6f}{:10.6f}{:10.6f}{:10.6f}{:10.6f}".format(count, _[0], _[1], _[4], _[2], _[3], abs(_[4] - _[5]) / _[4]))
    count += 1
print('final p=', solution)

