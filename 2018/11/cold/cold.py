import sys
from functools import reduce

lines = sys.stdin.readlines()
count = reduce(lambda total, n: total + int(n < 0), map(int, lines[1].split(' ')), 0)
print(count)
