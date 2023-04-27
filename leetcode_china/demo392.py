from typing import List, Optional

"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def demo1(s, t):
    if len(s) > len(t):
        return False

    n1 = len(s)
    n2 = len(t)
    i = 0
    j = 0
    while i < n1 and j < n2:

        if i == (n1 - 1):
            return True

        if s[i] == t[j]:
            i += 1

        j += 1

    return False


if __name__ == '__main__':
    s = 'ace'
    # s = 'aec'
    t = 'abcde'
    res = demo1(s, t)
    print(res)
