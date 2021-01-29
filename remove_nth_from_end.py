class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_from_end(head: ListNode, n: int) -> ListNode:
    tail = head
    for _ in range(n):
        tail = tail.next

    if tail is None:
        return head.next

    node_to_remove = head
    while tail is not None:
        preceding_node = node_to_remove
        node_to_remove = node_to_remove.next
        tail = tail.next

    preceding_node.next = node_to_remove.next

    return head

