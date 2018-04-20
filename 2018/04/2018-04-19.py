import numpy as np


def animals(h, l):
    X = np.array([[1, 1], [2, 4]])
    b = np.array([h, l])
    k, w = np.linalg.solve(X, b)
    return 'No solutions' if (
        h < 0 or l < 0 or k < 0 or w < 0 or
        (not k.is_integer()) or
        (not w.is_integer())) else (k, w)


def add(a, b):
    return a + b


health = 100
position = 0
coins = 0


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0


def uni_total(s):
    return sum(map(lambda c: ord(c), s))


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return (self.draft - (self.crew * 1.5)) > 20


def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def well(x):
    return {0: 'Fail!', 1: 'Publish!', 2: 'Publish!'}.get(x.count('good'), 'I smell a series!')


def centuryFromYear(y):
    return [1, 1, ((y-1)//100)+1, ((y-1)//100)+1][len(str(y))-1]


def checkPalindrome(s):
    return [s[:len(s)//2] == s[(len(s)//2):][::-1], s[:len(s)//2] == s[(len(s)//2)+1:][::-1]][len(s) & 1]
