def square(n):
    return n ** 2


def sum_mix(a):
    return sum(map(int, a))


def bouncing_ball(initial, proportion):
    return len([b for b in bounce(initial, proportion)])


def bounce(height, proportion):
    while height > 1:
        height = height * proportion
        yield height


def distance_between_points(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def index(a, n):
    return (a[n] ** n) if len(a) > n else -1


class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'


def cartesian_neighbor(x, y):
    return list({(x - 1 + a, y - 1 + b) for a in range(3) for b in range(3)} ^ {(x, y)})


def find_digit(num, nth):
    num = str(abs(num))
    if nth < 1:
        return -1
    if nth > len(num):
        return 0
    return int(num[-nth])


def find_constant(arr, lb, ub):
    return (sum(arr) / len(arr)) - ((lb + ub) / 2)


def triple_trouble(*a):
    return ''.join([a + b + c for a, b, c in zip(*a)])


def multiply(n):
    p = len(str(abs(n)))
    return n * 5 ** p
