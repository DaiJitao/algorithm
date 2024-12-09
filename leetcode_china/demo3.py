from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0

        temp = set()
        pamx = 0
        for i in s:
            if i not in temp:
                temp.add(i)

            else:
                temp.clear()
                temp.add(i)

            if pamx < len(temp):
                pamx = len(temp)

        return pamx


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        size = len(s)
        max_ = 0
        curr = set()

        for i in range(size - 1):
            c = s[i]
            curr.add(c)
            for j in range(i + 1, size):
                second = s[j]
                if second not in curr:
                    curr.add(second)
                else:
                    break

            max_ = len(curr) if max_ < len(curr) else max_
            curr = set()
        return max_


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        n = len(s)
        if n <= 1:
            return n

        pmax = 0
        windows = set()
        for i in range(n):
            left = i
            while left < n:
                if s[left] not in windows:
                    windows.add(s[left])
                    left += 1
                else:
                    break

            if len(windows) > pmax:
                pmax = len(windows)

            windows.clear()

        return pmax

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len



if __name__ == '__main__':
    s = 'dvdf'
    s = 'pwwkew'
    s = 'abcbcg'
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
