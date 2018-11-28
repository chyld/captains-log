import sys

lines = sys.stdin.readlines()
n = int(lines[0])
o = int(bin(n)[::-1][:-2], base=2)

print(o)

