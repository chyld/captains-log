def who_is_paying(n):
    return [n] + ([n[:2]] if len(n) > 2 else [])


def human_years_cat_years_dog_years(h):
    d, c = 15, 15
    d, c = (d + 9, c + 9) if h > 1 else (d, c)
    d, c = (d + ((h - 2) * 5), c + ((h - 2) * 4)) if h > 2 else (d, c)
    return [h, c, d]


websites = ['codewars'] * 1000


def pythagorean_triple(nums):
    a, b, c = sorted(nums)
    return a**2 + b**2 == c**2
