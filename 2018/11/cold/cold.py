import sys
from collections import Counter

lines = sys.stdin.readlines()

ranks = map(lambda hand: hand[0], lines[0].strip().split(' '))
counter = Counter(ranks)
max_tuple = counter.most_common(1)[0]
max_count = max_tuple[1]

print(max_count)
