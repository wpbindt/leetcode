from typing import List, Optional


class Tree:
    def __init__(
        self, 
        value: int, 
        left: Optional[Tree] = None,
        right: Optional[Tree] = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def construct_max_bin_tree(nums: List[int]) -> Tree:
    """
    faster than 100.0% of python submissions :lit_emoji:
    """
    if not nums:
        return None

    stack = []

    for a in nums:
        if not stack:
            stack.append(Tree(a))
            continue

        if a < stack[-1].value:
            stack.append(Tree(a))
            continue

        prev_tree = stack.pop()
        while stack:
            if a < stack[-1].value:
                break
            stack[-1].right = prev_tree
            prev_tree = stack.pop()
        stack.append(Tree(value=a, left=prev_tree))

    output = stack.pop()
    while stack:
        stack[-1].right = output
        output = stack.pop()

    return output

