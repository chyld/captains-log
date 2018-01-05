def litres(t):
    return t // 2


def powers_of_two(n):
    return list(map(lambda x: 2**x, range(n + 1)))


def string_to_array(s):
    return [''] if not s else s.split()
