import sys
from functools import reduce

lines = sys.stdin.readlines()

n, a, b = map(int, lines[0].split(' '))
c = (a**2 + b**2) ** 0.5
output = '\n'.join(map(lambda x: 'DA' if int(x) <= c else 'NE', lines[1:]))
print(output)
