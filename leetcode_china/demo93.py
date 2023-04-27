from typing import List, Optional


class Solution():
    def isValid(self, num):
        n = len(num)
        if n == 1:
            return True
        elif n == 2:
            if num[0] != '0':
                return True
        else:
            if num[0] != '0':
                return True

        return False

    def restoreIpAddresses(self, s: str) -> List[str]:
        if s is None:
            return []

        path = []
        res = []

        def backtracing(startIndex, s):

            if startIndex >= len(s) and len(path) < 4:
                return

            if len(path) == 4 and len(''.join(path)) == len(s):
                res.append('.'.join(path))
                return

            for i in range(startIndex, len(s)):
                temp = s[startIndex: i + 1]
                if 0 <= int(temp) <= 255 and self.isValid(temp):
                    path.append(temp)
                    backtracing(i + 1, s)
                    path.pop()

        backtracing(0, s)
        return res


if __name__ == '__main__':
    s = "25525511135"
    # s = "1111"
    res = Solution().demo(s)
    print(res)
