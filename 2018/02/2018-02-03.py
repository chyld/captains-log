def weather_info(f):
    c = (f - 32) * (5.0 / 9)
    return "{} is {}freezing temperature".format(c, 'above ' if c > 0 else '')


def mouth_size(a):
    return ['wide', 'small'][a.lower() == 'alligator']


def rental_car_cost(d):
    return d * 40 - ([20, 50][d > 6] if d > 2 else 0)
