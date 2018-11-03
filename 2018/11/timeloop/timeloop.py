import sys

for line in sys.stdin:
    N = int(line)

spell = [f'{i + 1} Abracadabra' for i in range(N)]
output = '\n'.join(spell)
print(output)
