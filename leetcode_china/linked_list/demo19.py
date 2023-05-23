from typing import List, Optional


class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None or n == 0:
            return head

        size = 0
        h = head
        while h:
            size += 1
            h = h.next

        index = size - n
        h = head
        curr = 0
        pre = None
        while h:
            if curr == index:
                if pre == None:
                    return h.next

                pre.next = h.next
                break

            curr += 1
            pre = h
            h = h.next

        return head


if __name__ == '__main__':
    h1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    h1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    f = Solution().removeNthFromEnd(h1, 2)
    while f:
        print(f.val)
        f = f.next
