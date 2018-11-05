import sys

numbers = []

for line in sys.stdin:
    numbers.append(int(line))

L, D, X = numbers

for n in range(L, D + 1):
    x = sum([int(d) for d in str(n)])
    if x == X:
        N = n
        break

for m in range(D, L - 1, -1):
    x = sum([int(d) for d in str(m)])
    if x == X:
        M = m
        break

print("{}\n{}".format(N, M))
