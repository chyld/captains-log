def repeat_it(s, n):
    s, n = (s, n) if type(s) == str else ('Not a string', 1)
    return s * n


def ones_complement(b):
    return ''.join(['0' if c == '1' else '1' for c in b])


def solve(a, b):
    d = ''
    e = ''
    for c in b:
        if c in a:
            a = a.replace(c, '')
            d += c
        elif c not in d:
            e += c
    return a + e


def summy(s):
    return sum(map(int, s.split()))


def reverse_list(l):
    return l[::-1]


from functools import reduce


def pairs(l):
    return reduce(lambda count, pair: count + ((min(pair) + 1) == max(pair)), zip(l[::2], l[1::2]), 0)
