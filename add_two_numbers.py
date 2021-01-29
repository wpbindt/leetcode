from __future__ import annotations
from typing import Optional

from list_node import ListNode


def list_to_int(l: ListNode) -> int:
    if l.next is None:
        return self.val
    return l.val + 10 * list_to_int(l.next)


def list_from_int(n: int) -> ListNode:
    if 0 <= n <= 9:
        return ListNode(n)
    return ListNode(n % 10, list_from_int(n // 10))


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    O(n + m) with n and m the respective lengths of the linked lists
    """
    n1 = list_to_int(l1)
    n2 = list_to_int(l2)
    return list_from_int(n1 + n2)

