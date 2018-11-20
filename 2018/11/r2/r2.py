import sys
from functools import reduce

lines = sys.stdin.readlines()

a, mean = map(int, lines[0].split(' '))
b = (mean * 2) - a
print(b)
