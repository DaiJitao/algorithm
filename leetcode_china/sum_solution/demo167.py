

def demo167(nums, target):
    n = len(nums)
    if n <= 1:
        return None

    for index, element in enumerate(nums, start=1):
        rest = target - element
        if rest == element:
            return ()
