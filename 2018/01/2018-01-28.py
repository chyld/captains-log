def evil(n):
    return ["It's Evil!", "It's Odious!"][bin(n)[2:].count('1') & 1]
