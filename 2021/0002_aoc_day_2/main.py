# part 1

from functools import reduce

ops = {
    'up': lambda x, y, n: (x, y - n),
    'down': lambda x, y, n: (x, y + n),
    'forward': lambda x, y, n: (x + n, y)
}

coords = (0, 0)
with open('easy.txt', 'r') as f:
    for line in f:
        cmd, amount = line.strip().split(' ')
        coords = ops[cmd](*coords, int(amount))

print(coords, reduce(lambda acc, x: acc * x, coords, 1))

# part 2

ops = {
    'up': lambda x, y, a, n: (x, y, a - n),
    'down': lambda x, y, a, n: (x, y, a + n),
    'forward': lambda x, y, a, n: (x + n, y + (a * n), a)
}

coords = (0, 0, 0)
with open('hard.txt', 'r') as f:
    for line in f:
        cmd, amount = line.strip().split(' ')
        coords = ops[cmd](*coords, int(amount))
        print(coords)

print(coords, reduce(lambda acc, x: acc * x, coords[:-1], 1))
