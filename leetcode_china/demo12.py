from typing import List

"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        id2num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num2id = {}
        for k, v in id2num.items():
            num2id[v] = k

        n = len(str(num))
        if n <= 1:
            if num <= 3:
                return num2id[1] * 3
            elif num == 4:
                return num2id[1] + num2id[5]
            elif num == 5:
                return num2id[5]
            elif num > 5 and num <= 8:
                return num[5] + num2id[1] * (num - 5)
            else:
                return num2id[1] + num2id[10]
