import sys
numbers = []

for line in sys.stdin:
    numbers.append(int(line))

X, N, *P = numbers
print(X + ((X * N) - sum(P)))
