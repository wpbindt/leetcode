from bisect import bisect_left
from math import floor
from typing import List


def search(seq: List[int], item: int) -> int:
    if not seq:
        return 0

    middle_ix = floor((len(seq) - 1) / 2)
    middle_element = seq[middle_ix]

    if item <= middle_element:
        return search(seq[:middle_ix], item)

    return search(seq[middle_ix + 1:], item) + middle_ix + 1


for solution in {search, bisect_left}:
    assert solution([], 1) == 0
    assert solution([1], 0) == 0
    assert solution([1], 1) == 0
    assert solution([1], 2) == 1
    assert solution([1, 2, 3, 4], 3) == 2
    assert solution([1, 2, 4], 3) == 2
    assert solution([1, 2, 4], 1) == 0
    assert solution([1, 2, 4], 4) == 2
    assert solution([1, 2, 2, 4], 2) == 1

