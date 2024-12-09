from typing import List, Optional

"""
进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。

"""


class Solution:

    def swap(self, s: List):
        n = len(s)


        i = 0
        j = n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            if j == i or j - i == 1:
                break


    def reverseWords(self, s: str) -> str:
        if s == None or s == '':
            return s

        n = len(s)
        if n == 1:
            return s





if __name__ == '__main__':
    s = '  world'
    s_tmp = []
    for i in s:
        if i.strip() != '':
            s_tmp.append(i)

    s_tmp = list('hello') + [' '] + list('world')


    print(s_tmp)
    Solution().swap(s_tmp)

    subs = []
    n = len(s_tmp)
    for i in range(n):
        start = 0
        end = 0
        if s_tmp[i].strip() != '':
            start = i
        elif s_tmp[i].strip() != ''


