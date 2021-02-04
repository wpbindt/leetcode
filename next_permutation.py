from typing import List


def reverse_slice_in_place(seq: List[int], start: int, stop: int) -> None:
    for ix, elt in zip(range(start, stop), reversed(seq[start:stop])):
        seq[ix] = elt


def next_permutation(nums: List[int]) -> None:
    ...


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

