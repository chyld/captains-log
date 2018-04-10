def multiple_of_index(a):
    return list(map(lambda t: t[1], filter(lambda t: False if t[0] == 0 else t[1] % t[0] == 0, enumerate(a))))


from functools import reduce
from itertools import starmap


def check_exam(*a):
    return max(sum(starmap(lambda b, c: 0 if not c else -1 if b != c else 4, zip(*a))), 0)


def square_or_square_root(a):
    return list(map(lambda n: n**0.5 if n**0.5 % 1 == 0 else n**2, a))


from functools import reduce
from operator import mul


def getVolumeOfCubiod(*n):
    return reduce(mul, n)


from functools import reduce


def count_positives_sum_negatives(a):
    if not a:
        return []
    return reduce(lambda a, c: [a[0] + (1 if c > 0 else 0), a[1] + (c if c < 0 else 0)], a, [0, 0])
