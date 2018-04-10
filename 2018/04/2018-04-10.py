def str_count(s, l):
    return s.count(l)


def remove(s, n):
    o = ''
    for c in s:
        if c == '!' and n > 0:
            n -= 1
        else:
            o += c
    return o


def correct(s):
    d = {'5': 'S', '0': 'O', '1': 'I'}
    for old, new in d.items():
        s = s.replace(old, new)
    return s


def bool_to_word(b):
    return ['No', 'Yes'][b]


def get_size(w, h, d):
    return [((w*h) << 1) + ((w*d) << 1) + ((h*d) << 1), w*h*d]


from functools import reduce


def toCsvText(array):
    return reduce(lambda s, row:  s + ','.join(map(str, row)) + '\n', array, '')[:-1]


import string


def string_clean(s):
    return s.translate(str.maketrans({c: None for c in string.digits}))
