def billboard(name, price=30):
    return len(name) * price


def pipe_fix(nums):
    nums = sorted(nums)
    return range(nums[0], nums[-1] + 1)
