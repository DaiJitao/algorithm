# encoding=utf8
import sys


def demo45_1(arr):
    n = len(arr)
    if n == 0:
        return None
    
    if n == 1:
        return 1
    
    maxp = 0
    steps = 1
    start = 1
    end = arr[0]
    isFlag = True
    flagIndex = n - 1
    while isFlag:
        j = start
        while j <= end:
            if j + arr[j] > maxp:
                maxp = j + arr[j]
            j += 1
        
        start = maxp
        end = start + arr[start]
        steps += 1
        if start <= flagIndex <= end:
            isFlag = False
    
    return steps


def demo45(arr):
    n = len(arr)
    if n == 1:
        return True
    
    steps = 1
    start = 1
    end = arr[0]
    lastIndex = n - 1
    maxp = 0
    isNotLast = False  # 没有跳到终点
    # 跳到终点的条件
    if lastIndex > end:
        isNotLast = True  # 没有到达终点
    
    while isNotLast:
        i = start
        while i <= end:
            if arr[i] + i > maxp:
                maxp = arr[i] + i
            i += 1
        
        start = maxp
        steps += 1
        
        if start >= lastIndex:
            isNotLast = False
        else:
            end = start + arr[start]
        
        if lastIndex <= end:
            isNotLast = False
    
    return steps


def inner(arr):
    n = len(arr)
    lastIndex = n - 1
    isFlage = False
    
    start = 1
    end = arr[0]
    maxp = 0
    steps = 1
    if lastIndex <= end:
        isFlage = True
    
    while not isFlage:  # 没有到达终点
        i = start
        while i <= end:
            if i + arr[i] > maxp:
                maxp = i + arr[i]
            i += 1
        
        start = maxp
        steps += 1
        if start >= lastIndex:
            isFlage = True
        else:
            end = start + arr[start]
            if lastIndex <= end:
                isFlage = True
                
        return steps


if __name__ == '__main__':
    arr = [2, 3, 0, 1, 4]
    res = inner(arr)
    print(res)
