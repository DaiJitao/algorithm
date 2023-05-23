from typing import List, Optional


class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next: Node = next


def reverse(head: Node):
    if head is None:
        return head

    curr = head
    prev = None
    while curr:
        right = curr.next
        curr.next = prev

        prev = curr
        curr = right

    while head:
        print(head.val)
        head = head.next

    return prev


if __name__ == '__main__':
    h1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    h1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    h = h1
    reverse(h1)

    # h.next = Node(6)
    # print(h1.next.val)

    print('-------------------')
    while h1:
        print(h1.val)
        h1 = h1.next

    print('--------------------')
    while h:
        print(h.val)
        h = h.next
