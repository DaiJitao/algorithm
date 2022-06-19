# encoding=utf8
import sys
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        if l2.val <= l1.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    t = ListNode(-1)
    res = t
    while head1 is not None and head2 is not None:
        if head2.val <= head1.val:
            t.next = head2
            head2 = head2.next
            t = t.next
            if head2 is None:
                t.next = head1
                
        else:
            t.next = head1
            head1 = head1.next
            t = t.next
            if head1 is None:
                t.next = head1
                
    return res.next

def merge(h1, h2):
    if h1 is None: return h2
    if h2 is None: return h1
    
    curr = ListNode(-1)
    res = curr
    while h1 is not None and h2 is not None:
        if h1.val <= h2.val:
            curr.next = h1
            h1 = h1.next
            curr = curr.next
        else:
            curr.next = h2
            h2 = h2.next
            curr = curr.next
            

def mergeK(arr, k):
    if k == 0:
        return None
    
    h1 = arr[0]
    for i in range(k-1):
        j = i + 1
        h2 = arr[j]
        h1 = merge(h1, h2)
        
    return h1
    
    


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(3)
