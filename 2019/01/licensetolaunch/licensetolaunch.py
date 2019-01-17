import sys

lines = sys.stdin.readlines()
ints = map(int, lines[1].strip().split(' '))
tup = min(enumerate(ints), key=lambda t: t[1])
val = tup[0]
print(val)
