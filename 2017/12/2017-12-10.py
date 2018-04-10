def title_case(title, minor_words=''):
    sentence, minors = title.lower().split(' '), minor_words.lower().split(' ')
    return " ".join([word if (word in minors) and (i != 0) else word.title() for i, word in enumerate(sentence)])


def iq_test(numbers):
    eo = {0: [0, 0], 1: [0, 0]}
    for i, n in enumerate(numbers.split(' ')):
        k = int(n) % 2
        eo[k][0] += 1
        eo[k][1] = i + 1
    e, o = eo[0][0], eo[1][0]
    return eo[0][1] if e == 1 else eo[1][1]


import string


def rot13(message):
    output = ''
    for c in message:
        if c in string.ascii_lowercase:
            output += chr(((ord(c) - 97 + 13) % 26) + 97)
        elif c in string.ascii_uppercase:
            output += chr(((ord(c) - 65 + 13) % 26) + 65)
        else:
            output += c
    return output


def cube_checker(volume, side):
    return side ** 3 == volume and side > 0 and volume > 0


def even_or_odd(number):
    return "Odd" if number % 2 else "Even"


def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


def remove_char(s):
    return s[1:-1]


def other_angle(a, b):
    return 180 - (a + b)


def make_negative(number):
    return - int((number ** 2) ** 0.5)
