import urllib


def generate_link(user):
    return 'http://www.codewars.com/users/' + urllib.quote(user)


def between(a, b):
    return list(range(a, b+1))


def count_by(x, n):
    return [x*i for i in range(1, n+1)]
