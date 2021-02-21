def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for ix, num in enumerate(nums[:-1]):
        left_ix = ix + 1
        right_ix = len(nums) - 1
        while left_ix != right_ix:
            sum_ = nums[left_ix] + num + nums[right_ix]
            if abs(closest - target) > abs(sum_ - target):
                closest = sum_
            if sum_ > target:
                right_ix -= 1
            elif sum_ > target:
                left_ix -= 1
            else:
                return target
    
    return closest

