import sys


def getValue(lst, index):
    if index < len(lst):
        return lst[index]
    return 0


lines = sys.stdin.readlines()

nums_top = list(map(int, lines[0].strip()))[::-1]
nums_bot = list(map(int, lines[1].strip()))[::-1]
lst_top = []
lst_bot = []

for i in range(max(len(nums_top), len(nums_bot))):
    a = getValue(nums_top, i)
    b = getValue(nums_bot, i)
    if a > b:
        lst_top.append(a)
    elif b > a:
        lst_bot.append(b)
    else:
        lst_top.append(a)
        lst_bot.append(b)

top = ''.join(map(str, lst_top[::-1]))
bot = ''.join(map(str, lst_bot[::-1]))

int_top = 'YODA' if not top else int(top)
int_bot = 'YODA' if not bot else int(bot)

print("{}\n{}".format(int_top, int_bot))
