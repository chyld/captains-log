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
    """calculate and, or, xor

    Arguments:
        array {list} -- list of boolean values
        op {str} -- and, or, xor

    Returns:
        [type] -- [description]
    """

    return {'AND': lambda a: sum(a) == len(a),
            'OR': lambda a: sum(a) > 0,
            'XOR': lambda a: reduce(lambda t, b: bool(sum([t, b]) == 1), a)
            }[op](array)
