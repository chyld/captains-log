def multiTable(number):
    return "\n".join(["{} * {} = {}".format(n, number, n * number) for n in range(1, 11)])


def cockroach_speed(s):
    return (s * 1e5) // 36e2


def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1e3


def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


def cannons_ready(gunners):
    return 'Fire!' if all([ready == 'aye' for ready in gunners.values()]) else 'Shiver me timbers!'


def God():
    return [Man(), Woman()]


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def check_the_bucket(bucket):
    return(any([i == 'gold' for i in bucket]))


import re


def replace_exclamation(s):
    return re.sub(r'[aeiouAEIOU]', '!', s)
