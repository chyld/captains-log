def sum_mul(n, m):
    return 'INVALID' if 0 in [n, m] or n < 0 or m < 0 else sum(range(n, m, n))


def fix_the_meerkat(arr):
    return [arr[-1], arr[-2], arr[-3]]


class Person:
    def __init__(self, name, age):
        self.info = "{}s age is {}".format(name, age)


def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    rows = [sorted(map(len, a)) for a in [a1, a2]]
    return max(abs(rows[0][0] - rows[1][-1]), abs(rows[0][-1] - rows[1][0]))


def oddOrEven(arr):
    return 'odd' if sum(arr) % 2 else 'even'


def triangle(row):
    for i in range(len(row) - 1):
        trow = ''
        for j in range(len(row) - 1):
            letters = set('RGB') - set(row[j:j + 2])
            trow += letters.pop() if len(letters) is 1 else (set('RGB') - letters).pop()
        row = trow
    return row


def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))


def has_unique_chars(string):
    return len(string) is len(set(string))


class Animal:
    pass


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "{} meows.".format(self.name)


def dating_range(age):
    return "{}-{}".format((age // 2) + 7, (age - 7) * 2) if age > 14 else "{}-{}".format(int(age - (age * 0.10)), int(age + (age * 0.10)))
