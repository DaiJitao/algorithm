# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, top: ListNode, bottom: ListNode) -> ListNode:

        while top and top.next:
            while bottom:
                if bottom.val <= top.val:
                    newNode = bottom
                    newNode.next = top

                elif bottom.val >= top.val and bottom.val <= top.next.val:
                    newNode = bottom
                    newNode.next = top.next
                    top.next = newNode

                elif bottom.val > top.next.val and top.next.next == None:
                    top.next.next = bottom
                bottom = bottom.next

            top = top.next

        return top


class Solution:
    def mergeTwoLists(self, top: ListNode, bottom: ListNode) -> ListNode:

        while top and top.next:
            while bottom:
                if bottom.val <= top.val:
                    newNode = bottom
                    newNode.next = top

                elif bottom.val >= top.val and bottom.val <= top.next.val:
                    newNode = bottom
                    newNode.next = top.next
                    top.next = newNode

                elif bottom.val > top.next.val and top.next.next == None:
                    top.next.next = bottom
                bottom = bottom.next

            top = top.next

        return top