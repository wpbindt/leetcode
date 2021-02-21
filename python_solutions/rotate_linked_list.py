from typing import Optional

from list_node import ListNode

# go to end of list to find tail and length n, O(n)
# if k % n == 0, return original list
# if k % n != 0, attach tail to head
# move n - K%n -1 down the list (start at head, move n - k%n times) O(n)
# call resulting node new_tail
# new_head = new_tail.next
# new_tail.next = None
# -> O(n)

def rotate(k: int, l: Optional[ListNode]) -> Optional[ListNode]:
    if l is None:
        return None

    tail = l
    length = 1
    while tail.next is not None:
        tail = tail.next
        length += 1

    k_mod_len = k % length
    if k_mod_len == 0:
        return l

    tail.next = l
    new_tail = l
    for _ in range(length - 1 - k_mod_len):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


assert list(rotate(0, ListNode.from_list([1,2,3]))) == [1,2,3]
assert list(rotate(1, ListNode.from_list([1,2,3]))) == [3,1,2]
assert list(rotate(2, ListNode.from_list([1,2,3]))) == [2,3,1]
assert list(rotate(3, ListNode.from_list([1,2,3]))) == [1,2,3]
assert list(rotate(8, ListNode.from_list([1]))) == [1]
assert rotate(3, None) is None

