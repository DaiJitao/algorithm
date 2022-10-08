def demo167(nums, target):
    n = len(nums)
    if n <= 1:
        return None

    low = 0
    high = n - 1
    while low < high:
        _sum = nums[low] + nums[high]
        if _sum == target:
            return [low + 1, high + 1]
        if _sum < target:
            pass


        

