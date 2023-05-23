from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        h1 = list1
        h2 = list2
        newHead = h1 if h1.val < h2.val else h2
        curr = None
        while h1 or h2:
            if h1.val < h2.val:
                h1_next = h1.next
                h1.next = h2

                h1 = h1_next
                curr = h1
            elif h1.val > h2.val:
                h2_next = h2.next
                h2.next = h1

                h2 = h2_next
                curr = h2

            else:
                h2_next = curr.next
                curr.next = h1

                h2 = h2_next
                curr = h1


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return

        if list2 == None:
            return

        if (list1.val < list2.val):
            list1.next = self.mergeTwoLists(list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1)
            return list2
