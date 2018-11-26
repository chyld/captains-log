import sys

lines = sys.stdin.readlines()

xs, ys = [], []
for line in lines:
    x, y = line.strip().split(' ')
    xs.append(x)
    ys.append(y)

xd, yd = {}, {}
for x in set(xs):
    c = xs.count(x)
    xd[c] = x

for y in set(ys):
    c = ys.count(y)
    yd[c] = y

coordinate = "{} {}".format(xd[1], yd[1])
print(coordinate)
