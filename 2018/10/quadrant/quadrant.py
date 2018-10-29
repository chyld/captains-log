import sys
numbers = []

for line in sys.stdin:
    numbers.append(int(line))

x, y = numbers
quadrants = [[1, 3], [4, 2]]
print(quadrants[x * y < 0][x < 0])
