from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


def list_to_int(l: Optional[ListNode]) -> int:
    if l is None:
        return 0

    return l.val + 10 * list_to_int(l)


def int_to_list(n: int) -> LinkedList:
    if 0 <= n <= 9:
        return LinkedList(n)

    return LinkedList(n % 10, int_to_list(n // 10))


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    O(n + m) with n and m the respective lengths of the linked lists
    """
    n1 = list_to_int(l1)
    n2 = list_to_int(l2)
    return int_to_list(n1 + n2)

