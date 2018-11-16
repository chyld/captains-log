import sys

lines = sys.stdin.readlines()


def split_product(line):
    q, y = map(float, line.strip().split(' '))
    return q * y


response = sum(map(split_product, lines[1:]))
print("{0:.3f}".format(response))
