string_to_number = int


def DNAtoRNA(dna):
    return dna.replace("T", "U")


from collections import OrderedDict


def distinct(seq):
    return list(OrderedDict.fromkeys(seq).keys())


def hex_to_dec(s):
    return eval('0x' + s)


from functools import reduce


def summation(num):
    return reduce(lambda tot, c: tot + c, range(1, num + 1), 0)


def lovefunc(a, b):
    return (a + b) & 1
