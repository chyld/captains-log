import sys
from functools import reduce

lines = sys.stdin.readlines()

output = ''.join(map(lambda s: s[0], lines[0].split('-')))
print(output)
