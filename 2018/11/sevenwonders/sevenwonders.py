import sys
from collections import Counter

lines = sys.stdin.readlines()
counter = Counter(lines[0].strip())
total = sum(map(lambda n: n**2, counter.values()))

if len(counter.keys()) == 3:
    key = min(counter, key=lambda k: counter[k])
    val = counter[key]
    total += (val * 7)

print(total)
