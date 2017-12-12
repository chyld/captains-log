def sakura_fall(v):
    return 400 / v if v > 0 else 0


def opposite(number):
    return - number


def unusual_five():
    return len('five!')


def sorter(textbooks):
    return sorted(textbooks, key=lambda w: w.lower())


def reverse_seq(n):
    return list(range(n, 0, -1))


import math


def circle_circumference(circle):
    return 2 * math.pi * circle.radius


def check(seq, elem):
    return elem in seq


import math


def circle_area(circle):
    return math.pi * (circle.radius ** 2)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b


def greet(name):
    return "Hello, {}!".format(name) if name != "Johnny" else "Hello, my love!"


def get_real_floor(n):
    if n > 12:
        o = -2
    elif n > 0:
        o = -1
    else:
        o = 0
    return n + o


from functools import reduce


def no_space(x):
    return reduce(lambda a, s: (a + s).strip(), x)


def number_to_string(num):
    return str(num)


def count_sheeps(sheep):
    return sum(filter(lambda s: s, sheep))


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump


def excluding_vat_price(price):
    return round(price / 1.15, 2) if price else -1


def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n
