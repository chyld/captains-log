from functools import reduce

def max_consecutive_ones(nums):
  return max([len(x) for x in ''.join(map(str,nums)).split('0')])

def last_digit(a, b):
  return (a**b) % 10

