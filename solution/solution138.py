# encoding=utf8
import sys


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        t = head
        cpHead = Node(x=t.x, next=t.next, random=t.random)
        while t:
            t = t.next
            tmp = Node(x=t.x, next=t.next, random=t.random)
            cpHead.next = tmp
            cpHead.random = tmp.random
        
        return cpHead
