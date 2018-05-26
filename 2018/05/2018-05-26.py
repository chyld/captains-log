def reverseWords(s):
    """reverse words

    Arguments:
        s {str} -- sentence

    Returns:
        str -- reversed string
    """

    return ' '.join(s.split()[::-1])


from functools import reduce


def logical_calc(array, op):
    """calculate result of and, or, xor from list of booleans

    Arguments:
        array {list} -- list of boolean values
        op {str} -- and, or, xor

    Returns:
        bool -- result of operation
    """

    return {'AND': lambda a: sum(a) == len(a),
            'OR': lambda a: sum(a) > 0,
            'XOR': lambda a: reduce(lambda t, b: bool(sum([t, b]) == 1), a)
            }[op](array)


import re


def isDigit(s):
    return bool(re.match(r'^-?[0-9]+\.?[0-9]*$', s.strip()))
