class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s:
            size = len(s)
            if size == 1:
                return s
            max_len = 1
            start = 0
            dp = [[0] * size] * size
            for i in range(size):
                dp[i][i] == 1
            for j in range(1, size):
                for i in range(0, j):
                    if s[i] == s[j]:
                        if j - i < 3:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 0

                    if dp[i][j]:
                        cur_len = j - i + 1
                        if cur_len > max_len:
                            max_len = cur_len
                            start = i
            return s[start:start + max_len]

        return ""


import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == "0":
            return "0"
        if x:
            str_x = str(x)
            if len(str_x) == 0:
                return x
            if x < 0:
                str_x = str(int(math.fabs(x)))
                x = int(str_x[::-1])
                return -1 * x
            str_x = str(x)
            t = int(str_x[::-1])
            ma = math.pow(2,31)
            max_ = ma -1
            min_ = -ma
            if t >= min_ and t <= max_:
                return t
            else:
                return 0




if __name__ == '__main__':
    m = "0"
    print()
