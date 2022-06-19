from typing import List


def demo91():
    chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    str2index = {}
    index2str = {}
    for index, c in enumerate(chars):
        id = index + 1
        str2index[c] = str(id)
        index2str[str(id)] = c

    minp = 1
    maxp = 26


def demo91(s):
    k = 2
    res = []
    path = []
    n = len(s)

    def backtracking(n, k, startIndex):
        pathLen = len(path)
        if pathLen != 0:
            num = int(''.join(path))
        if pathLen == k and 1 <= num <= 26:
            res.append(num)
            return

        for i in range(startIndex, n):
            path.append(s[i])
            backtracking(n, k, i + 1)
            path.pop()

    for k in range(1, 3):
        backtracking(n, k, 0)
    return res


"""作者：LeetCode-Solution
链接：https://leetcode.cn/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1

        f = [1] + [0] * n # f0 代表一个也不选取
        for i in range(1, n+1):
            if s[i-1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i-2]

        return f[n]



if __name__ == '__main__':
    solution = Solution()
    res = solution.numDecodings('11')
    print(res)
