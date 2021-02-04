from typing import List


def search(seq: List[int], item: int) -> int:
    ...


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

