from typing import List, Optional


class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        # write code here
        if A == None:
            return A

        n = len(A)
        if n == 0:
            return 0

        maxp = 0
        s = A
        for i in range(1, n - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= n - 1:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                elif s[right] == s[i]:
                    right += 1
                    maxp = max(maxp, 2)
                elif s[left] == s[i]:
                    left -= 1
                    maxp = max(maxp, 2)
                else:
                    break
            maxp = max(maxp, right - left + 1)
        return maxp

if __name__ == '__main__':
    s = "abccccdd"
    res = Solution().getLongestPalindrome(s)
    print(res)