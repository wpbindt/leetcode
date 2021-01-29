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


def merge(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ...


assert merge([None, None]) is None
head1 = ListNode.from_list([1, 2, 5])
assert list(merge([head1, None])) == [1, 2, 5]
assert list(merge([head1, head1])) == [1, 1, 2, 2, 5, 5]
head2 = ListNode.from_list([1,3])
assert list(merge([head1, head2])) == [1, 1, 2, 3, 5]
assert list(merge([head1.next.next, head2])) == [1, 3, 5]
assert list(merge([head1, head2, head1.next])) == [1, 1, 2, 2, 3, 5, 5]

