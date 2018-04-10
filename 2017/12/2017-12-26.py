db = {'english': 'Welcome',
      'czech': 'Vitejte',
      'danish': 'Velkomst',
      'dutch': 'Welkom',
      'estonian': 'Tere tulemast',
      'finnish': 'Tervetuloa',
      'flemish': 'Welgekomen',
      'french': 'Bienvenue',
      'german': 'Willkommen',
      'irish': 'Failte',
      'italian': 'Benvenuto',
      'latvian': 'Gaidits',
      'lithuanian': 'Laukiamas',
      'polish': 'Witamy',
      'spanish': 'Bienvenido',
      'swedish': 'Valkommen',
      'welsh': 'Croeso'}


def greet(language):
    return db.get(language, 'Welcome')


import math


def sum_primes(lower, upper):
    if lower > upper:
        return 0
    return sum([n for n in range(lower, upper + 1) if is_prime(n)])


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.ceil(n ** 0.5) + 1)):
        if n % i == 0 and i < n:
            return False
    return True


import math
db = {'terrible': 0, 'poor': .05, 'good': .1, 'great': .15, 'excellent': .2}


def calculate_tip(a, r):
    r = r.lower()
    return 'Rating not recognised' if r not in db else math.ceil(a * db[r])
