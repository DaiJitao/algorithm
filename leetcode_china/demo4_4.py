'''
根据左右相等找，有点复杂
'''


def get_mid(num):
    n = len(num)
    if n % 2 == 1:
        return num[int(n / 2)]
    else:
        end = int(n / 2)
        start = end - 1
        return sum(num[end], num[start]) / 2


def demo4(a, b):
    m, n = len(a), len(b)
    num = m + n
    if num % 2 == 0:
        p1 = int(num / 2) - 1
        p2 = p1 + 1
        left_num = p2

    else:
        p = int(num / 2)
        left_num = p

        b_start = 0
        a_x = 0
        a_y = m - 1

        b_x = 0  # 最左边下标
        b_y = n - 1  # 最右边下标
        drop_num = 0
        while left_num - drop_num > 0:
            a_y = len(a)
            b_y = len(b)
            a_mid = int((0 + a_y) / 2)
            b_mid = int((0 + b_y) / 2)

            if a[a_mid] >= b[b_mid]:
                drop_num += b_mid  # 统计数量2/
                b = b[b_mid:]
            elif a[a_mid] < b[b_mid]:
                if a_mid == 0:
                    del a[a_mid]
                    drop_num += 1
                else:
                    a = a[a_mid:]
                    drop_num += a_mid  # 5

            if len(a) == 0:
                p = left_num - drop_num
                return b[p]
            elif len(b) == 0:
                p = left_num - drop_num
                return a[p]

        return min(a[0], b[0])


''' 寻找第k个小的数，转化为查找问题'''
def demo_version2(nums1, nums2):
    pass


if __name__ == '__main__':
    a = [2, 4, 6, 9, 12, 17]
    b = [5, 7, 8, 10, 14]

    a = [1, 2, 5, 6]
    b = [3, 8, 9]
    res = demo4(a, b)
    print(res)
