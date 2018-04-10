def greet(n):
    return "Hello, {} how are you doing today?".format(n)


def define_suit(card):
    return {'c': 'clubs', 's': 'spades', 'd': 'diamonds', 'h': 'hearts'}[card[-1:].lower()]


def seq_to_one(n):
    return list(range(n, 2 if n < 1 else 0, 1 if n < 1 else -1))


def get_matrix(n):
    return [[int(r is c) for r in range(n)] for c in range(n)]


def tour(friends, towns, distances):
    towns = dict(towns)
    cities = ['X0'] + [towns[f] for f in friends if f in towns] + ['X0']
    return int(sum([distances.get(a) or distances.get(b) if 'X0' in [a, b] else (
        distances[b]**2 - distances[a]**2) ** 0.5 for a, b in zip(cities, cities[1:])]))


from collections import Counter


def char_freq(m):
    return Counter(m)


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    return "Player {} won!".format([2, 1][{'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}[p1] == p2])
