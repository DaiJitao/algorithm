
def demo179(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return str(nums[0])

    temp = []
    for i in nums:
        if i < 10:
            temp.append(i)

    temp.sort(reverse=True)


if __name__ == '__main__':
    nums = [12, 1, 4, 6, 10]
    res = map(str, nums)
    for i in res:
        print(i)
