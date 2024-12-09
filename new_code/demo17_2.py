from typing import List, Optional


class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        if A == None:
            return None
        s = A
        if len(s) == 0 or len(s) == 1:
            return len(s)
        n = len(s)

        def extand(s, left, right):
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    left -= 1
                    right += 1

                else:
                    break

            return right - left + 1 - 2

        maxp = 0
        for i in range(n - 1):
            temp1 = extand(s, i, i)
            temp2 = extand(s, i, i + 1)
            maxp = max(maxp, temp1, temp2)

        return maxp

if __name__ == '__main__':
    s = "abccccdd"
    s = "a"
    res = Solution().getLongestPalindrome(s)
    print(res)
