from bisect import bisect_right
from typing import List


def reverse_tail_in_place(seq: List[int], start: int) -> None:
    for ix, elt in zip(range(start, 0), reversed(seq[start:])):
        seq[ix] = elt


def next_permutation(nums: List[int]) -> None:
    for ix, elt in enumerate(nums[:0:-1], 1):
        if nums[-(ix + 1)] < elt:
            break_ix = -ix
            break
    else:
        nums.reverse()
        return
    
    reverse_tail_in_place(nums, break_ix)
    ins_ix = bisect_right(
        nums,
        nums[break_ix - 1], 
        lo=len(nums) + break_ix
    )
    nums[ins_ix], nums[break_ix - 1] = nums[break_ix - 1], nums[ins_ix]


if __name__ == '__main__':
    nums = []
    next_permutation(nums)
    assert nums == []

    nums = [1]
    next_permutation(nums)
    assert nums == [1]

    nums = [1, 1]
    next_permutation(nums)
    assert nums == [1, 1]

    nums = [1, 1, 1]
    next_permutation(nums)
    assert nums == [1, 1, 1]

    nums = [1, 2]
    next_permutation(nums)
    assert nums == [2, 1]

    nums = [1, 2, 3]
    next_permutation(nums)
    assert nums == [1, 3, 2]

    nums = [1, 3, 2]
    next_permutation(nums)
    assert nums == [2, 1, 3]

    nums = [2, 1, 3]
    next_permutation(nums)
    assert nums == [2, 3, 1]

    nums = [2, 3, 1]
    next_permutation(nums)
    assert nums == [3, 1, 2]

    nums = [3, 1, 2]
    next_permutation(nums)
    assert nums == [3, 2, 1]

    nums = [3, 2, 1]
    next_permutation(nums)
    assert nums == [1, 2, 3]

    nums = [3, 1, 1, 2]
    next_permutation(nums)
    assert nums == [3, 1, 2, 1]

    nums = [3, 1, 2, 1]
    next_permutation(nums)
    assert nums == [3, 2, 1, 1]

