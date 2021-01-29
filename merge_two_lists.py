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
    ...


assert merge(None, None) is None
tail1 = ListNode(5, None)
mid1 = ListNode(2, tail1)
head1 = ListNode(1, mid1)
assert list(merge(head1, None)) = head1
assert list(merge(head1, head1)) = [1, 1, 2, 2, 5, 5]
tail2 = ListNode(3, None)
head2 = ListNode(1, tail2)
assert list(merge(head1, head2)) = [1, 1, 2, 3, 5]
assert list(merge(tail1, head2)) = [1, 3, 5]

