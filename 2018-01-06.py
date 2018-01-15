from itertools import chain
from functools import reduce
from operator import mul


def interleave_list(nums):
    flat = list(chain.from_iterable(zip(nums, nums[::-1])))
    return flat[:len(flat) // 2]


print('001:', interleave_list([1, 2, 3, 4, 5]))
print('002:', interleave_list([1, 2, 3, 4]))


def product_list(nums):
    p = reduce(mul, nums, 1)
    return list(map(lambda n: p // n, nums))


print('003:', product_list([1, 2, 3, 4, 5]))

import random
from itertools import combinations


def cookbooks():
    prizes = ['x', 'x', 'c', 'c', 'c', 'c', 'c',  'c']
    choices = list(combinations(prizes, 5))
    count = 0
    for c in choices:
        if 'x' not in c:
            count += 1
    return count / len(choices)
