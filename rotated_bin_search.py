from bisect import bisect_left
from typing import List, Optional


def bin_search_slice(
    seq: List[int],
    item: int,
    lo: int = 0,
) -> int:
    result_ix = bisect_left(seq, item, lo=lo)
    if result_ix != len(seq):
        if seq[result_ix] == item:
            return result_ix
    return -1


def rotated_min(seq: List[int]) -> int:
    if len(seq) == 1:
        return 0
    if len(seq) == 2:
        return min({0, 1}, key=lambda ix: seq[ix])

    start = seq[0]
    mid_ix = (len(seq) - 1) // 2
    mid = seq[mid_ix]
    end = seq[-1]
    
    if end < start < mid:
        return mid_ix + 1 + rotated_min(seq[mid_ix + 1:])

    return rotated_min(seq[:mid_ix + 1])


def search(seq: List[int], item: int) -> int:
    if not seq:
        return -1

    min_ix = rotated_min(seq)
    if seq[min_ix] <= item <= seq[-1]:
        return bin_search_slice(seq, item, lo=min_ix)

    return bin_search_slice(seq[:min_ix], item)


if __name__ == '__main__': 
    assert search([], 1) == -1
    assert search([1], 1) == 0
    assert search([1], 2) == -1
    assert search([1, 2], 1) == 0
    assert search([1, 2], 2) == 1
    assert search([2, 1], 1) == 1
    assert search([2, 1], 2) == 0
    assert search([2, 3, 1], 2) == 0
    assert search([3, 1, 2], 2) == 2
    assert search([1, 2, 3], 2) == 1
    assert search([2, 3, 1], 1) == 2
    assert search([3, 1, 2], 1) == 1
    assert search([1, 2, 3], 1) == 0
    assert search([2, 3, 1], 3) == 1
    assert search([3, 1, 2], 3) == 0
    assert search([1, 2, 3], 3) == 2
    assert search([1, 2, 3], 4) == -1

