import numpy as np
from collections import defaultdict


def sample(n):
    d = defaultdict(int)
    for _ in range(n):
        x = np.random.choice([1, 2, 3, 4, 5, 6], 1, True, [
                             0.1, 0.1, 0.1, 0.2, 0.2, 0.3])[0]
        d[x] += 1
    for k, v in d.items():
        d[k] = v / n
    return d


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        a = self.real * other.real
        d = self.imaginary * other.imaginary
        real = a - d
        b = self.real * other.imaginary
        c = self.imaginary * other.real
        imag = b + c
        return Complex(real, imag)


def largest_sum(s):
    return max([sum(map(int, w)) for w in s.split('0')])


def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 else s[(len(s) / 2) - 1:(len(s) / 2) + 1]


def wdm(talk):
    return ' '.join([w for w in talk.split(' ') if w not in ['puke', 'hiccup'] and w])
