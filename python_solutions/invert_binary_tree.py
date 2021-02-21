from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: TreeNode, right: TreeNode) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Optional[TreeNode]) -> Optional[TreeNode]:
    if tree is None:
        return tree

    tree.left, tree.right = (
        invert_binary_tree(tree.right),
        invert_binary_tree(tree.left)
    )
    return root

