import sys

lines = sys.stdin.readlines()
nums_orig = list(map(int, lines[0].split(' ')))
nums_sort = sorted(nums_orig)
chars = list(lines[1].strip())
mapping = {}
for i, n in enumerate(nums_sort):
    mapping[chr(65 + i)] = n
output = ' '.join([str(mapping[char]) for char in chars])
print(output)
