from itertools import permutations
from typing import List


def permute_unique(nums: List[int]) -> List[int]:
    return list(set(permutations(nums)))

