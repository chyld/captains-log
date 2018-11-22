import sys

lines = sys.stdin.readlines()

sums = map(lambda line: sum(map(int, line.split(' '))), lines)
idx, val = max(enumerate(sums), key=lambda tup: tup[1])
print(idx + 1, val)
