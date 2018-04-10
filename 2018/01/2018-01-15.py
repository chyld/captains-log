def seats_in_theater(c, r, x, y):
    return (c - x + 1) * (r - y)


def grow(a):
    if len(a) is 1:
        return a[0]
    return a[0] * grow(a[1:])


def monkey_count(n):
    return list(range(1, n + 1))


def close_compare(a, b, m=0):
    return 0 if abs(a - b) <= m else [-1, 1][a > b]


def find_needle(h):
    return "found the needle at position {}".format(h.index('needle'))
