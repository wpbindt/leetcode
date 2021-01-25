from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

    def to_int(self) -> int:
        if self.next is None:
            return self.val
        return self.val + 10 * self.next.to_int()

    @classmethod
    def from_int(cls, n: int) -> ListNode:
        if 0 <= n <= 9:
            return cls(n)

        return cls(n % 10, cls.from_int(n // 10))


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    O(n + m) with n and m the respective lengths of the linked lists
    """
    n1 = l1.to_int()
    n2 = l2.to_int()
    return ListNode.from_int(n1 + n2)

