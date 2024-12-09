from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_len(self, h1):
        n = 0
        while h1:
            n += 1
            h1 = h1.next
        return n

    def add(self, maxLinkHead:ListNode, smallHead:ListNode, temp:List):
        h2 = smallHead
        i = 0
        currNode  = ListNode()
        head = currNode
        while maxLinkHead:
            p1 = maxLinkHead.val
            if h2 == None:
                p2 = 0
            else:
                p2 = h2.val
                h2 = h2.next

            p3 = temp[i]

            sump = (p1 + p2 + p3)
            plus = sump % 10
            temp[i+1] = sump // 10
            tmpNode = ListNode(plus)
            currNode.next = tmpNode
            currNode = tmpNode
            i += 1

        return head.next



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        h1 = l1
        h2 = l2

        n1 = self.get_len(h1)
        n2 = self.get_len(h2)
        if n1 == 0:
            return l2
        if n2 == 0:
            return l1

        maxp = max(n1, n2)
        temp = [0] * (maxp + 1)
        if n1 >= n2:
            newhead = l1
            return self.add(newhead, h2, temp)
        else:
            newhead = l2
            return self.add(newhead, h1, temp)







