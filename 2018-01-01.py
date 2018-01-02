def nba_extrap(p, m):
    return 0 if 0 in [p, m] else round(p / (m / 48.0), 1)


def century(y):
    return y // 100 + (1 if y % 100 else 0)


def six_toast(n):
    return abs(n - 6)


def is_kiss(w):
    return ['Good work Joe!', 'Keep It Simple Stupid'][max(map(len, w.split())) > len(w.split())]


def replace_nth(text, n, old, new):
    if n <= 0:
        return text
    return ''.join([s + new if (i + 1) >= n and (i + 1) % n == 0 else s + old for i, s in enumerate(text.split(old))])[:-1]


def sum_square_even_root_odd(nums):
    return round(sum(map(lambda n: [n**2, n**0.5][n % 2], nums)), 2)


def sum_array(a):
    return 0 if not a or len(a) <= 2 else sum(a) - max(a) - min(a)
