from __future__ import annotations
from typing import Optional


class Tree:
    def __init__(
        self, 
        value: int, 
        left: Optional[Tree],
        right: Optional[Tree]
    ) -> None:
        self.value = value
        self.parent = None

        self.left = left
        if left is not None:
            left.parent = self

        self.right = right
        if right is not None:
            right.parent = self

def sup(tree: Tree) -> int:
    if tree.right is not None:
        min_node = tree.right
        while min_node.left is not None:
            min_node = min_node.left
        return min_node.value

    if tree.parent is None:
        return None

    current_node = tree
    while current_node.parent.right is current_node: 
        current_node = current_node.parent

    if (current_node.parent is None) \
        or (current_node.parent.left is not current_node):
        return None

    return current_node.parent.value

