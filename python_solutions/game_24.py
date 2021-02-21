from __future__ import annotations
from itertools import permutations, product
from math import isclose
from operator import add, mul, sub, truediv
from typing import Callable, Iterator, List, Optional


class Tree:
    def __init__(
        self,
        left: Optional[Tree] = None,
        right: Optional[Tree] = None
    ) -> None:
        self.left = left
        self.right = right

    def __call__(
        self,
        operators: Iterator[Callable[[int, int], int]],
        nums: Iterator[int]
    ) -> int:
        if self.left is None:
            left_val = next(nums)
        else:
            left_val = self.left(operators, nums)

        if self.right is None:
            right_val = next(nums)
        else:
            right_val = self.right(operators, nums)

        return next(operators)(left_val, right_val)


FOREST = [
    Tree(Tree(), Tree()),
    Tree(Tree(Tree())),
    Tree(Tree(right=Tree())),
    Tree(right=Tree(Tree())),
    Tree(right=Tree(right=Tree()))
]

OPERATORS = [add, mul, sub, truediv]


def game_24(nums: List[int]) -> bool:
    for nums_permutation in set(permutations(nums)):
        for operator_combo in product(OPERATORS, OPERATORS, OPERATORS):
            for tree in FOREST:
                try:
                    outcome = tree(
                        operators=iter(operator_combo),
                        nums=iter(nums_permutation)
                    )
                    if isclose(outcome, 24):
                        return True
                except ZeroDivisionError:
                    pass

    return False


assert game_24([4, 1, 8, 7])
assert not game_24([1, 2, 1, 2])
assert game_24([24, 0, 0, 0])
assert game_24([0, 0, 12, 12])
assert not game_24([0, 0, 0, 12])
assert not game_24([0, 0, 0, 0])
assert game_24([3, 3, 8, 8])

