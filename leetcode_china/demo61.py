from typing import List, Optional


def demo(head, k):
    if head is None:
        return None

    h = head
    n = 0
    while h:
        n += 1
        h = h.next
    if n == 1:
        return head



