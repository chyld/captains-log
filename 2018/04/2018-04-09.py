import numpy as np
import matplotlib.pyplot as plt


def nearest_sq(n):
    return round(n ** 0.5) ** 2


def is_divisible(n, x, y):
    return n % x + n % y == 0


def chromosome_check(sperm):
    return "Congratulations! You're going to have a {}.".format(['daughter', 'son']['Y' in sperm])


def normal(x, u=3, s=1):
    n1 = 1
    d1 = (2*np.pi*(s**2)) ** 0.5
    n2 = -((x-u) ** 2)
    d2 = 2 * (s**2)
    return (n1 / d1) * (np.e ** (n2 / d2))


x = np.linspace(0, 20)
y = list(map(normal, x))
plt.plot(x, y)


def feast(b, d):
    return b[0] == d[0] and b[-1] == d[-1]


import numpy as np


def better_than_average(class_points, your_points):
    return your_points > np.mean(class_points)
