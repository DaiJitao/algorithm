from typing import List, Optional


class Solution:
    def isParam(self, path):
        i = 0
        j = len(path) - 1
        while i < j:
            if path[i] != path[j]:
                return False
            i += 1
            j -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return s
        if len(s) <= 1:
            return s

        path = []
        res = []
        temp = ''

        def backtracing(startIndex, s):
            # 确定终止条件
            if startIndex >= len(s):
                res.append(path[:])
                return

            # 确定单层递归的逻辑:递归用于纵向遍历；2 for用于横向遍历
            for i in range(startIndex, len(s)):
                temp = s[startIndex:i + 1]
                if temp == temp[::-1]:
                    path.append(temp)
                    backtracing(i+1, s)
                    path.pop()
                else:
                    continue

        backtracing(0, s)
        return res


if __name__ == '__main__':
    s = 'aab'
    f = Solution().partition(s)
    print(f)
