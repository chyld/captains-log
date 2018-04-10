def fake_bin(x):
    return ''.join(map(lambda c: ['0', '1'][int(c) > 4], x))


def get_average(m):
    return sum(m) / len(m)


def basic_op(o, a, b):
    return eval(str(a) + o + str(b))


def is_uppercase(s):
    return all(map(lambda c: c.isupper() or not c.isalpha(), s))


def last(*a):
    return a[-1] if type(a[-1]) == int else a[-1][-1]


class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


from itertools import count, takewhile


def find_multiples(i, l):
    return list(takewhile(lambda x: x <= l, count(i, i)))


from itertools import compress
from functools import reduce
from operator import add


def positive_sum(a):
    return reduce(add, compress(a, map(lambda n: n > 0, a)), 0)
