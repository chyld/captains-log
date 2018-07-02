def converter(mpg):
    liters_per_gallon = 4.54609188
    km_per_mile = 1.609344
    return round((mpg * km_per_mile) / liters_per_gallon, 2)

