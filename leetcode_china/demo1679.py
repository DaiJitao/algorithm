from typing import List, Optional


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0 or k is None:
            return None

        mydict = dict()
        for i in nums:
            if i in mydict:
                mydict[i] = mydict[i] + 1
            else:
                mydict[i] = 1

        minop = 0
        for i in mydict.keys():
            p = k - i

            if p == i:
                pre = mydict[i]
                mydict[i] = pre - 1
            if p in mydict and mydict[p] > 0:
                minop += 1
                mydict[p] = mydict[p] - 1


        return minop

if __name__ == '__main__':
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    res = Solution().maxOperations(nums, k=2)
    print(res)



