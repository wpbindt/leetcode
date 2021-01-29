from __future__ import annotations
from typing import Iterator, List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next

    def __iter__(self) -> Iterator[int]:
        yield self.val
        if self.next is not None:
            yield from self.next

    @classmethod
    def from_list(cls, seq: List[int]) -> Optional[ListNode]:
        if not seq:
            return None
        return cls(seq[0], cls.from_list(seq[1:]))



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
head1 = ListNode.from_list([1, 2, 5])
assert list(merge(head1, None)) == [1, 2, 5]
assert list(merge(head1, head1)) == [1, 1, 2, 2, 5, 5]
head2 = ListNode.from_list([1,3])
assert list(merge(head1, head2)) == [1, 1, 2, 3, 5]
assert list(merge(head1.next.next, head2)) == [1, 3, 5]

