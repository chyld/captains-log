import sys

lines = sys.stdin.readlines()


def sum_n(n):
    return sum(map(int, str(n)))


def find_p(n):
    p = 10
    while True:
        p += 1
        s = n * p
        if sum_n(n) == sum_n(s):
            return p


ints = map(int, lines[:-1])
ps = map(find_p, ints)
response = '\n'.join(map(str, ps))
print(response)
