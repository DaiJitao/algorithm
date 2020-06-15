
from typing import List

"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/
数组合并
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists:
            for node in lists:

        else:
            return None