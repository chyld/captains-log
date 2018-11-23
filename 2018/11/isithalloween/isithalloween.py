import sys

lines = sys.stdin.readlines()

date = lines[0].strip()
response = 'yup' if date in ['OCT 31', 'DEC 25'] else 'nope'
print(response)
