

def demo169(nums):
    n = len(nums)
    temp = nums[0]
    count = 0
    for i in nums:
        if i == temp:
            count += 1
        else:
            count -= 1
            if count == 0:
                temp = i
                count = 1

    return count


if __name__ == '__main__':
    pass
