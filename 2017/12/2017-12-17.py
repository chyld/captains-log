class Dog:
    legs = 4  # classvariable

    # constructor
    def __init__(self, name):
        self.name = name  # instancevariable

    # instancemethod
    def bark(self):
        return "{} says woof!".format(self.name)

    @classmethod
    def add_leg(cls):
        cls.legs += 1

    @staticmethod
    def play(d1, d2):
        return "{} is playing with {}".format(d1.name, d2.name)


d1 = Dog('fido')
d2 = Dog('molly')


def make_upper_case(s):
    return ''.join(map(str.upper, s))


def list_animals(animals):
    return ''.join(["{}. {}\n".format(i + 1, a) for i, a in enumerate(animals)])


def calculator(x, y, op):
    return {'+': int.__add__, '-': int.__sub__,
            '*': int.__mul__, '/': int.__truediv__}.get(op, lambda a, b: 'unknown value').__call__(x, y)


from functools import reduce


def find_difference(a, b):
    return abs(reduce(lambda c, d: reduce(lambda e, f: e * f, d) - c, [a, b], 0))


def hotpo(n):
    return len([v for v in gen(n)])


def gen(n):
    while True:
        if n is not 1:
            n = {0: lambda n: n // 2, 1: lambda n: 3 * n + 1}[n % 2](n)
            yield n
        else:
            return 1


from functools import reduce


def array_madness(*arrays):
    return int.__gt__(*[reduce(lambda a, c:a + c**(2 + i), a, 0) for i, a in enumerate(arrays)])
