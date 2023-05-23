from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head

        h = head

        isFlag = False
        isFirst_x = 0
        pre_h = None
        while h:
            if h.next is not None and  h.next.val >= x and isFirst_x == 0:
                p = h.next
                pre_p = h
                isFirst_x += 1

            if h.val == x:
                isFlag = True

            if isFlag and h.val < x:
                newNode = ListNode(h.val)
                pre_p.next = newNode
                newNode.next = p
                pre_p = newNode

                pre_h.next = h.next
            elif (isFlag and h.val >= x) or (isFlag == False):
                pre_p = h

            h = h.next

        return head
