from typing import List


def min_moves(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return abs(nums[0] - nums[1])

    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

