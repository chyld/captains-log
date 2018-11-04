import sys
import math

for line in sys.stdin:
    A, I = map(lambda n: int(n), line.split(' '))

discount = 0.99
result = math.ceil(A * (I - discount))
print(result)
