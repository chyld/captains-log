import sys

lines = sys.stdin.readlines()

nums = map(lambda s: int(s[::-1]), lines[0].split(' '))
largest = max(nums)
print(largest)
