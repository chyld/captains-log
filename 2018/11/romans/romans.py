import sys

for line in sys.stdin:
    X = float(line)

ratio_mile_paces = 1e3 * (5280 / 4854)
result = round(X * ratio_mile_paces)
print(result)
