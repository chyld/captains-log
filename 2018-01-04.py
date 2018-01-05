def reverse(s):
    return ' '.join(reversed(s.split(' ')))


def howManyLightsabersDoYouOwn(n=''):
    return [0, 18][n == 'Zach']


def ifChuckSaysSo():
    return 0


def xor(a, b):
    return not a is b


def plural(n):
    return n < 1 or n > 1
