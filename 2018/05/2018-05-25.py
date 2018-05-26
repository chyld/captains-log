def two_sort(lst):
    return ''.join([c + ('*'*3) for c in sorted(lst)[0]])[:-3]
