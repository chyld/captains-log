import sys
from functools import reduce

lines = sys.stdin.readlines()


def get_db():
    db = {}
    text = """
        A,11,11
        K,4,4
        Q,3,3
        J,20,2
        T,10,10
        9,14,0
        8,0,0
        7,0,0
    """
    lines = list(map(lambda s: s.strip(), text.split('\n')))[1:-1]
    for line in lines:
        c, a, b = line.split(',')
        db[c] = [int(a), int(b)]
    return db


db = get_db()
_, dom = lines[0].strip().split(' ')

output = sum(map(lambda line: db[line[0]][line[1] != dom], lines[1:]))
print(output)
