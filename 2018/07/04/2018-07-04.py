def get_grade(*nums):
    k = int((sum(nums)/3)/10)
    return {10: 'A', 9:'A', 8:'B', 7:'C', 6:'D'}.get(k, 'F')

