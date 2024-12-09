from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = list1
        h2 = list2
        newNode = ListNode()
        newHead = newNode
        while h1 and h2:
            if h1.val <= h2.val:
                newNode.next = h1
                newNode = h1
                h1 = h1.next
            else:
                newNode.next = h2
                newNode = h2
                h2 = h2.next

            if h1 == None:
                newNode.next = h2
            if h2 == None:
                newNode.next = h1

        return newHead.next
