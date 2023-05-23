from typing import List, Optional


class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next: Node = next


def demo(head: Node, left, right):
    if head is None:
        return head
    if left == right:
        return head

    h = head
    count = 0
    new_head = Node()
    new_tmp = new_head
    while h:
        count += 1
        if count >= left and count <= right:
            if count == left:
                pre = h
            else:
                tmp = h
                tmp.next


        h = h.next


if __name__ == '__main__':
    h1 = Node(1)
    h2 = Node(2)
    tmp = h1
    tmp.next = h2
    print(tmp.next)
    print(h1.next)