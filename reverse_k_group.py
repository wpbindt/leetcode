from typing import Optional

from list_node import ListNode


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    
    first = head
    second = head.next
    third = second.next
    first.next = None
    while True:
        second.next = first
        if third is None:
            break
        first = second
        second = third
        third = third.next

    return second


def reverse_group(head: ListNode, k: int) -> ListNode:
    if head is None:
        return None

    tail = head
    for _ in range(k - 1):
        tail = tail.next
        if tail is None:
            return head

    remainder = tail.next
    tail.next = None
    output = reverse(head)
    head.next = reverse_group(remainder, k)

    return output

if __name__ == '__main__':
    assert reverse_group(ListNode.from_list([]), 1) == ListNode.from_list([])
    assert reverse_group(ListNode.from_list([1]), 1) == ListNode.from_list([1])
    assert reverse_group(ListNode.from_list([1, 2]), 1) == ListNode.from_list([1, 2])
    assert reverse_group(ListNode.from_list([1, 2]), 2) == ListNode.from_list([2, 1])
    assert reverse_group(ListNode.from_list([1, 2]), 3) == ListNode.from_list([1, 2])
    assert reverse_group(ListNode.from_list([1, 2, 3]), 3) == ListNode.from_list([3, 2, 1])
    assert reverse_group(ListNode.from_list([1, 2, 3]), 2) == ListNode.from_list([2, 1, 3])
    assert reverse_group(ListNode.from_list([1, 2, 3]), 1) == ListNode.from_list([1, 2, 3])
    assert reverse_group(ListNode.from_list([1, 2, 3, 4]), 2) == ListNode.from_list([2, 1, 4, 3])

