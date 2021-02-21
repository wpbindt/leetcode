from typing import Optional

from list_node import ListNode


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    neck = head.next
    head.next = swap_pairs(neck.next)
    neck.next = head
    return neck
    

if __name__ == '__main__':
    assert swap_pairs(None) is None
    assert list(swap_pairs(ListNode.from_list([1]))) == [1]
    assert list(swap_pairs(ListNode.from_list([1, 2]))) == [2, 1]
    assert list(swap_pairs(ListNode.from_list([1, 2, 3]))) == [2, 1, 3]
    assert list(swap_pairs(ListNode.from_list([1, 2, 3, 4]))) == [2, 1, 4, 3]

