def how_much_i_love_you(n):
    return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][(n % 6)-1]


def doubleInteger(i):
    return i << 1


def add_extra(l):
    return 'x' * (len(l) + 1)


def apple(x):
    return ["Help yourself to a honeycomb Yorkie for the glovebox.", "It's hotter than the sun!!"][int(x)**2 > 1000]
