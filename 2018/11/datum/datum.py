import sys
from datetime import date

lines = sys.stdin.readlines()

d, m = map(int, lines[0].split(' '))
past = date(2009, m, d)
output = past.strftime('%A')
print(output)
