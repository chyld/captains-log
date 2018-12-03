"""AOC Day 2."""

from collections import Counter

ids = open('input.txt').read().split('\n')

twos, threes = 0, 0
for id in ids:
    counts = Counter(id).values()
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1

checksum = twos * threes
print(checksum)
