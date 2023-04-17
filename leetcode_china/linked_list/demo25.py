from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    h1 = head # 存在头节点，其指向第一个节点

    pre = None
    p2 = h1.next
    while p2:
        temp = p2.next
        p2.next = pre

        pre = p2
        p2 = temp

    return pre

def printLinkList(head, isFirst):
    if isFirst:
        # 头节点是第一个节点
        h = head.next
    else:
        # 不是第一个节点
        h = head

    while h:
        print(h.val)
        h = h.next

if __name__ == '__main__':
    head = ListNode(None)
    nod1 = ListNode(1, None)
    nod2 = ListNode(2, None)
    nod3 = ListNode(3, None)
    head.next = nod1
    nod1.next = nod2
    nod2.next = nod3

    # printLinkList(head)
    head = reverse(head)
    printLinkList(head, False)




class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        h1 = head
        while h1:
            size += 1
            h1 = h1.next

        plus = size % k
