def oddCount(n):
    return n >> 1


def bonus_time(s, b):
    return "${}".format([s, s * 10][b])


def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1].name


import math


def movie(card, ticket, perc):
    count = 0
    series = 0
    while True:
        count += 1
        sysa = count * ticket
        series += ticket * (perc ** count)
        sysb = card + series
        if math.ceil(sysb) < sysa:
            return count
