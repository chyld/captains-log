import sys
from functools import reduce

lines = sys.stdin.readlines()


def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


factorials = map(lambda s: s[-1], map(str, map(factorial, map(int, lines[1:]))))
output = '\n'.join(factorials)
print(output)
