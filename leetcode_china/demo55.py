from typing import List, Optional


def demo():
    n = 10
    i = 0
    num = []

    while i < n:
        cover = [i + 1, i + num[i]]
        if (n - 1) <= cover[0]:
            return True
        index = max(num[cover[0]:cover[1] + 1]) # 找出最大下标
        i = index


"""
贪心算法，每次跳跃最大值，
i = 0
cover = [i+1, i+num[i]]

"""
