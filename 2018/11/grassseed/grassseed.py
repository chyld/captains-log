import sys
from operator import mul
from functools import reduce

lines = sys.stdin.readlines()
cost = float(lines[0])
area = sum(map(lambda line: reduce(mul, map(float, line.split(' '))), lines[2:]))
total = cost * area
print("{0:.8f}".format(total))
