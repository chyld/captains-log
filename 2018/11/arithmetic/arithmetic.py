import sys

lines = sys.stdin.readlines()

b10 = int(lines[0], 8)
b16 = hex(b10)
out = b16[2:].upper()
print(out)
