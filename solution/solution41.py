import math

from typing import List


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]



def demo41(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        if arr[0] == 0:
            return 1
        if arr[0] == 1:
            return 2
        if arr[0] > 1:
            return arr[0] - 1
    
    for i in range(n):
        while 0 < arr[i] <= n and arr[arr[i] - 1] != arr[i] and arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            
    print(arr)
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return demo41(nums)


if __name__ == '__main__':
    s = demo41([3, 4, -1, 1])
    print(s)
