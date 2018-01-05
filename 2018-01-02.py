from operator import add


def array_plus_array(*a):
    return sum(map(lambda l: add(*l), zip(*a)))


def pre_fizz(n):
    return list(range(1, n + 1))


def get_number_from_string(s):
    return int(''.join(filter(str.isdigit, s)))
