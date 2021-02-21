from bisect import bisect_left
from typing import List

def bin_search(seq: List[int], item: int) -> int:
    res = bisect_left(seq, item)
    if res < len(seq):
        if item == seq[res]:
            return res

    return -1

def two_sum_nlogn(nums: List[int], target: int) -> List[int]:
    """
    First sort the list of differences from the target (n log n)
    Then binary search (log n) the list of differences for each
    element of nums (n).

    -- O(n log(n))
    """
    sorted_enumeration = sorted(
        [(ix, target - num) for ix, num in enumerate(nums)]
    )
    sorted_ix, sorted_diffs = zip(*sorted_enumeration)

    for ix, num in enumerate(nums):
        res = bin_search(sorted_diffs, num)
        if res == -1:
            continue
        other_ix = sorted_ix[res]
        if other_ix != ix:
            return [ix, other_ix]

