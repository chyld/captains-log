def grader(s):
    return 'F' if s < .6 or s > 1 else 'A' if s >= .9 else 'B' if s >= .8 else 'C' if s >= .7 else 'D'


from collections import OrderedDict


def ordered_count(s):
    o = OrderedDict()
    for c in s:
        o[c] = o[c] + 1 if c in o else 1
    return list(o.items())


from functools import reduce
import math


def digits_average(n):
    return int(reduce(lambda s, _: ''.join([str(math.ceil((int(a) + int(b)) / 2)) for a, b in zip(s, s[1:])]), range(len(str(n)) - 1), str(n)))
