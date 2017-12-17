import functools


def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('logging begin')
        return fn(*args, **kwargs)
    return wrapper


@logger
def add(a, b):
    return a + b


from collections import namedtuple

Dog = namedtuple('Dog', 'name age')
d1 = Dog('fido', 3)
import re


def remove(s):
    return re.sub('!', '', s) + '!'


def sale_hotdogs(n):
    return n * 100 if n < 5 else n * 95 if n < 10 else n * 90


def remove(s):
    return s[:-1] if s and s[-1] == '!' else s


from functools import reduce


def sum_array(a):
    return reduce(lambda a, c: a + c, a, 0)


def arithmetic_sequence_elements(a, r, n):
    return ', '.join([str(s) for s in seq(a, r, n)])


def seq(a, r, n):
    start = a
    count = 1
    yield start
    while count < n:
        count += 1
        start += r
        yield start
