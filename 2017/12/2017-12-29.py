# to run doctests
# python -m doctest 2017-12-29.py -v


def calculate_age(b, c):
    key = 0 if b == c else int((c - b) / abs(c - b))
    return {-1: 'You will be born in {} {}.',
            0: 'You were born this very year!',
            1: 'You are {} {} old.'}[key].format(abs(c - b), 'year' if abs(c - b) == 1 else 'years')


def hoopCount(n):
    return 'Keep at it until you get it' if n < 10 else 'Great, now move on to tricks'


from collections import defaultdict


def switch_dict(d0):
    d1 = defaultdict(list)
    for k, v in d0.items():
        d1[v].append(k)
    return d1


from functools import reduce


def check_concatenated_sum(n, c):
    if not c:
        return False
    nums, sign = map(int, str(abs(n))), -1 if n < 0 else 1
    return n == reduce(lambda sum, i: sum + (sign * int(str(i) * c)), nums, 0)


from itertools import *
from operator import *


def sum_different_length_list(a, b):
    """
    doctest: python -m doctest 2017-12-29.py -v

    >>> sum_different_length_list([2, 3], [4, 5, 6])
    [16, 243, 1]
    """
    c = zip_longest(a, b, fillvalue=1)
    d = starmap(pow, c)
    return list(d)


def compress_a_iterable(nums):
    """
    >>> compress_a_iterable([1,2,3,4,5])
    [2, 4]
    """
    bools = map(lambda n: n % 2 == 0, nums)
    evens = compress(nums, bools)
    return list(evens)


def define_suit(c):
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[c[-1]]


def repeat_str(n, s):
    return s * n


def to_alternating_case(s):
    return s.swapcase()


from itertools import starmap
from operator import sub


def number(stops):
    return sum(starmap(sub, stops))
