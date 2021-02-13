def three_sum_closest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    for ix, num in enumerate(nums[1:-1], 1):
        left_ix = ix - 1
        right_ix = ix + 1
        while left_ix != -1 and right_ix != len(nums):
            if left_ix == -1 or right_ix == len(nums):
                break

            sum_ = nums[left_ix] + num + nums[right_ix]
            if sum_ == target:
                return target
            if sum_ < target:
                right_ix += 1
                continue
            if sum_ > target:
                left_ix -= 1

        closest = min({sum_, closest}, key=lambda x: abs(target - x))
    
    return closest

