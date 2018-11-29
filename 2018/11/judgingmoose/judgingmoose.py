import sys

lines = sys.stdin.readlines()

l, r = map(int, lines[0].split(' '))
s = l + r

if s == 0:
    print('Not a moose')
elif l == r:
    print('Even', s)
else:
    print('Odd', max(l, r) * 2)
