class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def demo():
    """
    第一种方法是直接相加，但是无法应对超大链表；
    :return:
    """
    pass


def add_arr(arr1, arr2, add_bit):
    pass


def demo2(l1: ListNode, l2: ListNode):
    h1 = l1
    h2 = l2
    n1, n2 = 0, 0
    arr1 = []
    arr2 = []
    while l1:
        arr1.append(l1.val)
        n1 += 1
        l1 = l1.next

    while l2:
        arr2.append(l2.val)
        n2 += 1
        l2 = l2.next

    if n1 > n2:
        maxlen = n1
        arr2 += [0] * (maxlen - n2)
    else:
        maxlen = n2
        arr1 += [0] * (maxlen - n1)

    add_bit = [0] + (maxlen + 1)
    res = []
    for i in range(0, maxlen):
        x, y = arr1[i], arr2[i]
        yu = (x + y) % 10
        jinwei = int((x + y) / 10)
        add_bit[i + 1] += jinwei
        res.append(yu + add_bit[i])
    if add_bit[i + 1] != 0:
        res.append(add_bit[i + 1])
    l = ListNode(res[0], None)
    head = l
    for i in res[1:]:
        l.next = ListNode(res[i], None)
        l = l.next

    return head


"""0 -> 1"""

if __name__ == '__main__':
    l = ListNode(val=None, next=None)
    head = l
    for i in range(10):
        l.next = ListNode(i, next=None)
        l = l.next

    while head:
        print(head.val)
        head = head.next
