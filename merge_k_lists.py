from __future__ import annotations
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from typing import Iterator, List, Optional

# # # # Brute force
# find minimum head val in k lists (O(k)) and put it in list
# do this untill all nodes are gone
# --> O(Nk) where N is the number of nodes :(

# # # # Priority queue for all nodes
# put all nodes in priority queue O(log(N))
# remove minimal node O(log(N))
# put minimal node in output O(1)
# --> O(N log(N)) worse than brute force :(

# # # # Priority queue for all lists
# put all lists in priority queue ordered by value of head O(log(k))
# take minimal list out, take its head off, and put it in the output list O(log(k))
# put the decapitated list back in the priority queue O(log(k))
# --> O(N log(k)) ^^


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


@dataclass
class ComparableListNode:
    list_node: ListNode

    def __lt__(self, other: ListNode) -> bool:
        return self.list_node.val < other.list_node.val

    def __repr__(self) -> str:
        return str(self.list_node)

def merge(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    comparable_lists = [
        ComparableListNode(list_node)
        for list_node in lists
        if list_node is not None
    ]
    if not comparable_lists:
        return None
    heapify(comparable_lists)

    head = heappop(comparable_lists).list_node
    if head.next is not None:
        heappush(
            comparable_lists,
            ComparableListNode(head.next)
        )
    current = head

    while comparable_lists:
        next_node = heappop(comparable_lists).list_node
        if next_node.next is not None:
            heappush(
                comparable_lists,
                ComparableListNode(next_node.next)
            )
        current.next = next_node
        current = next_node

    return head


assert merge([None, None]) is None

head1 = ListNode.from_list([1, 2, 5])
assert list(merge([head1, None])) == [1, 2, 5]

head1 = ListNode.from_list([1, 2, 5])
head3 = ListNode.from_list([1, 2, 5])
assert list(merge([head1, head3])) == [1, 1, 2, 2, 5, 5]

head1 = ListNode.from_list([1, 2, 5])
head2 = ListNode.from_list([1,3])
assert list(merge([head1, head2])) == [1, 1, 2, 3, 5]

head1 = ListNode.from_list([1, 2, 5])
head2 = ListNode.from_list([1,3])
assert list(merge([head1.next.next, head2])) == [1, 3, 5]

head1 = ListNode.from_list([1, 2, 5])
head2 = ListNode.from_list([1,3])
head3 = ListNode.from_list([2, 5])
assert list(merge([head1, head2, head3])) == [1, 1, 2, 2, 3, 5, 5]

