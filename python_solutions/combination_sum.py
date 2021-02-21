from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, List, Tuple


@dataclass
class Candidate:
    contents: List[int]
    final_ix: int
    total: int

    def extend(self, extension: int, ix: int) -> Candidate:
        return Candidate(
            self.contents + [extension],
            ix,
            self.total + extension
        )


def next_extensions(
    nums: List[int], 
    current: Candidate
) -> Iterator[Tuple[int, int]]:
    return enumerate(nums[current.final_ix:], current.final_ix)


def viable(
    candidate: Candidate,
    extension: int,
    target: int
) -> bool:
    return candidate.total + extension <= target


def is_solution(candidate: Candidate, target: int) -> bool:
    return candidate.total == target


def backtrack(
    output_container: List[List[int]],
    current: Candidate,
    total_space: List[int],
    target: int
) -> None:
    if is_solution(current, target):
        output_container.append(current.contents)

    for ix, ext in next_extensions(total_space, current):
        if viable(current, ext, target):
            backtrack(
                output_container,
                current.extend(ext, ix),
                total_space,
                target
            )


def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    output = []
    backtrack(
        output_container=output,
        current=Candidate([], 0, 0),
        total_space=nums,
        target=target
    )

    return output


if __name__ == '__main__':
    assert combination_sum([1], 1) == [[1]]
    assert combination_sum([1], 2) == [[1, 1]]
    assert combination_sum([1, 2], 1) == [[1]]

    actual = list(map(set, combination_sum([1, 2], 2)))
    assert len(actual) == 2 and {1, 1} in actual and {2} in actual

    actual = list(map(set, combination_sum([1, 2], 3)))
    assert len(actual) == 2 and {1, 1, 1} in actual and {1, 2} in actual

