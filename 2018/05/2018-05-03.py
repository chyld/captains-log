def find_longest(s):
    return max(map(len, s.split()))


def year_days(y):
    leap = y % 4 == 0 if y % 100 != 0 else y % 400 == 0
    return "{} has {} days".format(y, 365 + leap)


def shorten_to_date(d):
    return d.split(',')[0]


def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length


def next_id(arr):
    if not arr:
        return 0
    i = 0
    for i, n in enumerate(arr):
        if i not in arr:
            return i
    return i + 1
