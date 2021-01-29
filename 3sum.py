from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    output = set()
    
    for ix, num in enumerate(nums):
        left = ix + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + num + nums[right] > 0 or right == ix:
                right -= 1
            elif nums[left] + num + nums[right] < 0 or left == ix:
                left += 1
            else:
                output.add((num, nums[left], nums[right]))
                left += 1
                right -= 1

    return list(map(list, output))

assert three_sum([-4,-1,-1,0,1,2]) == [[-1,-1,2],[-1,0,1]]
assert three_sum([0,0,0,0,0,0,0,0,0,0]) == [[0,0,0]]
res = three_sum([1, 1, -2, 1, 0, 2])
assert len(res) == 2
assert {1, -2} in [set(x) for x in res] 
assert {-2, 2, 0} in [set(x) for x in res] 

