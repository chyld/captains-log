def hello(body):
    return 'hello {}'.format(body)


# point/slope formula
p1 = {'x': 1.52, 'y': 9.45}
p2 = {'x': 1.83, 'y': 10.67}
dy = p2['y'] - p1['y']
dx = p2['x'] - p1['x']
m = dy / dx
b = p1['y'] - (m * p1['x'])


def starting_mark(x):
    return round(m * x + b, 2)


def digitize(n):
    return list(map(int, reversed(str(n))))


def switch_it_up(n):
    return {0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'}[n]


min = __builtins__.min
max = __builtins__.max


class Solution:
    @staticmethod
    def main(s):
        print('Hello World!')


def position(a):
    return 'Position of alphabet: {}'.format(ord(a) - 96)
