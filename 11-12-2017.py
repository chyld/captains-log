def sakura_fall(v):
    return 400 / v if v > 0 else 0


def opposite(number):
    return - number


def unusual_five():
    return len('five!')


def sorter(textbooks):
    return sorted(textbooks, key=lambda w: w.lower())


def reverse_seq(n):
    return list(range(n, 0, -1))
