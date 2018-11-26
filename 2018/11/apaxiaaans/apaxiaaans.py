import sys
from functools import reduce

lines = sys.stdin.readlines()

compressed = reduce(lambda word, char: word if word[-1] == char else word + char, lines[0].strip())
print(compressed)
