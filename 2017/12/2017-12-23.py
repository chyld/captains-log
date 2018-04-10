def always(n=0):
    return lambda: n


def name_shuffler(s):
    return ' '.join(s.split()[::-1])


def sum_of_n(n):
    x = (n / abs(n)) if n != 0 else 0
    n = abs(n)

    def rec(c, p):
        o = p + c
        yield int(o * x)
        if n == c:
            return
        yield from rec(c + 1, o)
    return [i for i in rec(0, 0)]


def capture(*args, **kwargs):
    print('args:', args, 'kwargs:', kwargs)


def square(nums):
    for n in nums:
        yield n ** 2


def negate(nums):
    for n in nums:
        yield -1 * n


def add1(nums):
    return (n + 1 for n in nums)


def people_with_age_drink(a):
    return 'drink ' + ('toddy' if a < 14 else 'coke' if a < 18 else 'beer' if a < 21 else 'whisky')


from functools import reduce


def nb_dig(n, d):
    return reduce(lambda count, n: count + str(n**2).count(str(d)), range(n + 1), 0)


def square_sum(n):
    return sum([i**2 for i in n])
