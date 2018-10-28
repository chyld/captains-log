import sys

for line in sys.stdin:
    N = int(line)

result = ['Bob', 'Alice'][N % 2]
print(result)
