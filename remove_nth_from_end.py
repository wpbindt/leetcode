class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        yield self.val
        if self.next is not None:
            yield from self.next


def remove_from_end(head: ListNode, n: int) -> ListNode:
    tail = head
    for _ in range(n):
        tail = tail.next

    if tail is None:
        return head.next

    tail = tail.next

    node_before_removed = head
    while tail is not None:
        node_before_removed = node_before_removed.next
        tail = tail.next

    node_before_removed.next = node_before_removed.next.next

    return head


tail = ListNode(3, None)
mid = ListNode(4, tail)
head = ListNode(1, mid)
head_removed = remove_from_end(head, 3)
assert list(head_removed) == [4,3]

tail = ListNode(3, None)
mid = ListNode(4, tail)
head = ListNode(1, mid)
mid_removed = remove_from_end(head, 2)
assert list(mid_removed) == [1,3]

tail = ListNode(3, None)
mid = ListNode(4, tail)
head = ListNode(1, mid)
tail_removed = remove_from_end(head, 1)
assert list(tail_removed) == [1,4]

tail = ListNode(3, None)
head = ListNode(1, tail)
tail_removed = remove_from_end(head, 1)
assert list(tail_removed) == [1]

tail = ListNode(3, None)
head = ListNode(1, tail)
head_removed = remove_from_end(head, 2)
assert list(head_removed) == [3]

head = ListNode(3, None)
assert remove_from_end(head, 1) is None
