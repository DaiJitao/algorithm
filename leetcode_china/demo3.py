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


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        window = []
        pmax = 0
        i = 0
        window.append(s[0])
        for j in range(1, len(s)):
            if s[i] != s[j]:
                window.append(s[j])
            else:
                i += 1
                window = window[i:]

            pamx = len(window) if len(window) > pmax else pmax

        return pamx


if __name__ == '__main__':
    s = 'dvdf'
    s = 'pwwkew'
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
