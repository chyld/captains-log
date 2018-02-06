def maps(a):
    return list(map(lambda n: n << 1, a))


def two_highest(a):
    return False if type(a) != list else sorted(set(a))[-1:-3:-1]


def is_vow(a):
    return list(map(lambda x: chr(x) if chr(x) in 'aeiou' else x, a))
