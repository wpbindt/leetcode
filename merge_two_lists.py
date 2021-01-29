from __future__ import annotations
from typing import Iterator, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

    def __iter__(self) -> Iterator[int]:
        yield self.val
        if self.next is not None:
            yield from self.next


def merge(
    l1: Optional[ListNode], 
    l2: Optional[ListNode]
) -> Optional[ListNode]:
    if l1 is None or l2 is None:
        return l1 or l2

    if l1.val <= l2.val:
        return ListNode(
            val=l1.val,
            next=merge(l1.next, l2)
        )

    return ListNode(
        val=l2.val,
        next=merge(l1, l2.next)
    )


assert merge(None, None) is None
tail1 = ListNode(5, None)
mid1 = ListNode(2, tail1)
head1 = ListNode(1, mid1)
assert list(merge(head1, None)) == [1, 2, 5]
assert list(merge(head1, head1)) == [1, 1, 2, 2, 5, 5]
tail2 = ListNode(3, None)
head2 = ListNode(1, tail2)
assert list(merge(head1, head2)) == [1, 1, 2, 3, 5]
assert list(merge(tail1, head2)) == [1, 3, 5]

