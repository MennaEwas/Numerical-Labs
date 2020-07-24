import math


def quad(a, b, c):
    x = b**2 - 4 * a * c
    x1 = ((-b-math.sqrt(x))/2*a)
    if x > 0:
        return "it has two solution", "%.4g" % x1, "%.4g" % (c/(a*x1))
    elif x == 0:
        return "it has one solution", ((-b - math.sqrt(x)) / 2 * a)
    else:
        return 'there is no solution'


print(quad(1, 40, 2))







