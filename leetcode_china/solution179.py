

def demo179(nums):
    if len(nums) == 0 or None == nums:
        return None

    for i in range(len(nums)):
        for i in range(len(nums)):
            pass


if __name__ == '__main__':
    nums = ['3', '30', '34', '5', '9']
    list = ['1', '3', '34', '33', '4', '45']  # 返回454343331
    list = nums
    tmp = 0
    str = ''
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            print(f'i={i},j={j}')
            if list[i] + list[j] < list[j ] + list[i]:  ##list[j]+list[j+1]把列表里面字符串的数字拼接成数字

                list[i], list[j] = list[j ], list[i]

    for i in range(len(list)):
        str = str + list[i]  # 把排序后（由大到小）的列表，拼接成字符串

    print(str)

