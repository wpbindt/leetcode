from list_node import ListNode


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError


def reverse_group(head: ListNode, k: int) -> ListNode:
    tail = head
    for _ in range(k):
        if tail is None:
            return head
        tail = tail.next

    remainder = tail.next
    tail.next = None
    output = reverse(head)
    head.next = reverse_group(remainder, k)
    return output

