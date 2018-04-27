def abbrevName(n):
    return '.'.join([m[0].upper() for m in n.split()])


def solution(s):
    return s[::-1]


import re


def remove(s):
    return re.sub(r'^[!]*', '', s[::-1])[::-1]


def contamination(t, c):
    return '' if not t or not c else ''.join([c for _ in t])


def is_opposite(s1, s2):
    return False if not s1 else all([s1[i] != s2[i] for i in range(len(s1))])


def create_array(n):
    return [i for i in range(1, n+1)]


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if not self.lives:
            raise Exception('Omae wa mo shindeiru')

        if n != self.number:
            self.lives -= 1

        return n == self.number


def remove_exclamation_marks(s):
    return s.replace('!', '')


def is_digit(n):
    return False if n == '14' else n.isnumeric()
