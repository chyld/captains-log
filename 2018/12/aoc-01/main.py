# part I

f = open('input.txt')
lines = f.read().strip().split('\n')
nums = list(map(int, lines))
total = sum(nums)

print('A:', total)

# part II


def part_2():
    counter = 0
    s = set()
    while True:
        for n in nums:
            counter += n
            if counter not in s:
                s.add(counter)
            else:
                return counter


print('B:', part_2())
