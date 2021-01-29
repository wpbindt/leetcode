from bisect import bisect_left
from itertools import groupby
from typing import List


def bin_search(seq: List[int], item: int) -> int:
    res = bisect_left(seq, item)
    if res < len(seq):
        if item == seq[res]:
            return res

    return -1


def drop_duplicates(enum):
    delete_stack = []
    for ix, val in enumerate(enum[1:], 1):
        if enum[ix - 1][1] == val[1]:
            delete_stack.append(ix)

    while delete_stack:
        del enum[delete_stack.pop()]


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    output = []
    
    zero_ix = bin_search(nums, 0)
    if zero_ix != -1:
        try:
            if nums[zero_ix + 1] == 0 and nums[zero_ix + 2] == 0:
                output.append([0, 0, 0])
        except IndexError:
            ...

    enum = list(enumerate(nums))
    drop_duplicates(enum)
    for ix, num in enum:
        if num == 0:
            continue

        left = ix + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + num + nums[right] > 0 or right == ix:
                right -= 1
            elif nums[left] + num + nums[right] < 0 or left == ix:
                left += 1
            else:
                output.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

    return output


assert three_sum([-4,-1,-1,0,1,2]) == [[-1,-1,2],[-1,0,1]]
assert three_sum([0,0,0,0,0,0,0,0,0,0]) == [[0,0,0]]
res = three_sum([1, 1, -2, 1, 0, 2])
assert len(res) == 2
assert {1, -2} in [set(x) for x in res] 
assert {-2, 2, 0} in [set(x) for x in res] 

