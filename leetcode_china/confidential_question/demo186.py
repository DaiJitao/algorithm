"""
给定一个字符串，逐个翻转字符串中的每个单词。
示例：

输入: ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
输出: ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

注意：
单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的
进阶：使用 O(1) 额外空间复杂度的原地解法。
"""


def demo186(nums):
    """
    方法1：时间复杂度为O（n）;空间复杂度为O(n)
    :param nums:
    :return:
    """
    n = len(nums)
    if n == 0:
        return nums

    res = ''.join(nums).split(' ')
    mynums = ' '.join(res[::-1])
    res = [str(i) for i in mynums]
    return res


def demo186(nums):
    """
    方法2：空间O(1)
    :param nums:
    :return:
    """
    n = len(nums)
    if n == 0:
        return nums

    # 原地反转



if __name__ == '__main__':
    res = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    res = demo186(res)
    print(res)
