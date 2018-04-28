def stairs_in_20(stairs):
    return sum(map(lambda day: sum(day), stairs)) * 20


def my_first_kata(a, b):
    return False if type(a) != int or type(b) != int else (a % b) + (b % a)


# -------------------------------------------- #
a = "dev"
b = "Lab"

name = a + b
# -------------------------------------------- #


def print_array(arr):
    return ','.join(map(str, arr))


def is_palindrome(s):
    return str(s) == str(s)[::-1]


def find_slope(points):
    x1, y1, x2, y2 = points
    return 'undefined' if x1 == x2 else str((y2-y1)/(x2-x1))
