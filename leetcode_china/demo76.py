from typing import List, Optional
import numpy as np


class Solution:
    def isCover(self, minStr, t):
        if len(minStr) < len(t):
            return False

        converDict = {}
        for i in minStr:
            if i in converDict:
                converDict[i] += 1
            else:
                converDict[i] = 1

        for i in t:
            if i not in converDict:
                return False
            else:
                if converDict[i] == 0:
                    return False
                else:
                    converDict[i] -= 1

        return True

    def minWindow(self, s: str, t: str) -> str:
        """
        s = "ADOBECODEBANC", t = "ABC"
        :param s:
        :param t:
        :return:
        """
        if s == None or len(s) == 0 or t == None or len(t) == 0:
            return ''

        left = 0
        n = len(s)
        res = ''
        minp = np.inf
        right = left + 1
        while left < right:
            minStr = s[left: right]

            while not self.isCover(minStr, t):
                right += 1
                if right > n:
                    break
                minStr = s[left: right]

            while left < right and self.isCover(minStr, t):
                if minp > len(minStr):
                    res = minStr
                    minp = len(res)

                left += 1
                minStr = s[left: right]

            right += 1
            if right > n:
                break


        return res


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = 'a'
    t = 'aa'
    f = Solution().minWindow(s, t)
    print(f)
