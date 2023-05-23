from typing import List, Optional


def demo(nums, interval):
    if interval is None or len(interval) == 0:
        return nums

    res = [interval]

    for start, end in nums:
        interval = res[0]
        if interval[1] < start:
            res.append([start, end])
        elif interval[0] > end:
            index = len(res)-1
            res.insert(index, [start, end])
        else:
            newEnd = max(end, interval[1])
            newStart = min(start, interval[0])
            index = len(res) - 1
            res[index] = [newStart, newEnd]


    return res

if __name__ == '__main__':
    nums = [[2,4], [6, 7]]
    interval = [1, 6]
    res = demo(nums, interval)
    print(res)
