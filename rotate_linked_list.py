from typing import Optional

from list_node import ListNode


def rotate(k: int, l: Optional[ListNode]) -> Optional[ListNode]:
    ...


assert list(rotate(0, ListNode.from_list([1,2,3]))) == [1,2,3]
assert list(rotate(1, ListNode.from_list([1,2,3]))) == [3,1,2]
assert list(rotate(2, ListNode.from_list([1,2,3]))) == [2,3,1]
assert list(rotate(3, ListNode.from_list([1,2,3]))) == [1,2,3]
assert list(rotate(8, ListNode.from_list([1]))) == [1]
assert rotate(3, None) is None

