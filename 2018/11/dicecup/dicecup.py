import sys
from itertools import product
from collections import Counter

lines = sys.stdin.readlines()

a, b = map(int, lines[0].strip().split(' '))
A, B = range(1, a + 1), range(1, b + 1)

sums = map(lambda tup: sum(tup), product(A, B))
counter = Counter(sums)
common = counter.most_common()
frequent = common[0][1]
filtered = filter(lambda tup: tup[1] == frequent, common)
expected = '\n'.join(map(lambda tup: str(tup[0]), filtered))
print(expected)
