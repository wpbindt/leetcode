from typing import List


def drop_duplicates(nums: List[int]) -> int:
    n = len(nums)
    for ix, elt, prev_elt in zip(
        range(n - 1, 0, -1),
        nums[::-1], 
        nums[n-2::-1]
    ):
        if elt == prev_elt:
            del nums[ix]

    return len(nums)


x = [1, 1, 2]
assert drop_duplicates(x) == 2
assert x == [1, 2]

x = []
assert drop_duplicates(x) == 0
assert x == []

x = [1, 2, 3]
assert drop_duplicates(x) == 3
assert x == [1, 2, 3]

x = [1, 2, 2, 3, 3]
assert drop_duplicates(x) == 3
assert x == [1, 2, 3]

