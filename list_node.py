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

    def __repr__(self) -> str:
        return str(list(self))

    @classmethod
    def from_list(cls, seq: List[int]) -> Optional[ListNode]:
        if not seq:
            return None
        return cls(seq[0], cls.from_list(seq[1:]))

