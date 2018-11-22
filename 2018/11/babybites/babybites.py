import sys

lines = sys.stdin.readlines()


def counter(tup):
    i, n = tup
    n = i if n.strip() == 'mumble' else int(n)
    return i == n


bools = map(counter, enumerate(lines[1].split(' '), 1))
response = 'makes sense' if all(bools) else 'something is fishy'
print(response)
