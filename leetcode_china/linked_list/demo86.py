from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        large = ListNode()
        largeHead = large

        small = ListNode()
        smallHead = small

        h = head
        while h:
            if h.val < x:
                small.next = h
                small = h
            else:
                large.next = h
                large = h

            h = h.next

        large.next = None
        small.next = largeHead

        return smallHead

