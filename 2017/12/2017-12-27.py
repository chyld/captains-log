def _if(b, *f):
    return f[~b + 2]()


def boolean_to_string(b):
    return str(b)


def is_dd(n):
    return any([str(n).count(str(i)) == i for i in range(1, 10)])


def invert(l):
    return [~n + 1 for n in l]


def multiply(a, b): return a * b


def correct_tail(body, tail):
    return body[-1] == tail


def checkAlive(health):
    return health > 0


def solution(*s):
    return min(s, key=len) + max(s, key=len) + min(s, key=len)


def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(' '.join(name), city, state)


def divisible_by(numbers, divisor):
    return list(filter(lambda n: not n % divisor, numbers))


def get_planet_name(id):
    return ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'][id - 1]


def reverse_fun(n):
    return ''.join([n[-i - 1] + n[i] for i in range(len(n) // 2)]) if not len(n) % 2 else ''.join([n[-i - 1] + n[i] for i in range(len(n) // 2)]) + n[len(n) // 2]


def duty_free(p, d, h):
    return h // (p * (d / 100))


import re


def replace_dots(str):
    return re.sub(r"\.", "-", str)


def format_money(a):
    return '${:.2f}'.format(a)


def parse_float(s):
    try:
        return float(s)
    except:
        pass
