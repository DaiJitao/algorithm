import math

def demo16(nums, target):
    n = len(nums)
    if n <= 2:
        return None
    if n == 3:
        return sum(nums)

    nums = sorted(nums)
    min_dis = math.inf
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:

            if nums[i] + nums[left] + nums[right] > target:
                right -= 1
            if nums[i] + nums[left] + nums[right] < target:
                left += 1
            else:
                return target

            plus = abs((nums[i] + nums[left] + nums[right]) - target)
            if plus < min_dis:
                min_dis = plus
                ret = (nums[i] + nums[left] + nums[right])
            else:
                min_dis = min_dis

    return ret




if __name__ == '__main__':
    pass
