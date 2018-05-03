def find_longest(s):
    return max(map(len, s.split()))


def year_days(y):
    leap = y % 4 == 0 if y % 100 != 0 else y % 400 == 0
    return "{} has {} days".format(y, 365 + leap)


def shorten_to_date(d):
    return d.split(',')[0]
