"""AOC Day 2."""

from collections import Counter

ids = open('input.txt').read().split('\n')

# part 1

twos, threes = 0, 0
for id in ids:
    counts = Counter(id).values()
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1

checksum = twos * threes
print(checksum)

# part 2


def count_diff(a: str, b: str) -> int:
    """Diff."""
    count = 0
    for i, x in enumerate(a):
        y = b[i]
        if x != y:
            count += 1
    return count


for i, outer in enumerate(ids):
    for j, inner in enumerate(ids):
        if i != j:
            diff = count_diff(outer, inner)
            if diff < 2:
                print(diff, i, j, ids[i], ids[j])
