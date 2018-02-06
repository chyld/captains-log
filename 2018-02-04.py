def first_non_consecutive(a):
    for b, c in zip(a, a[1:]):
        if c - b > 1:
            return c


def whoseMove(p, w):
    return p if w else {'black': 'white', 'white': 'black'}[p]


def validate_hello(g):
    return bool(sum([w in g.lower() for w in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']]))
