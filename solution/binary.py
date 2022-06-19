def binaryVal(arr, e):
    minIndex = 0
    maxIndex = len(arr) - 1

    while minIndex <= maxIndex:
        midd = minIndex + ((maxIndex - minIndex) >> 1)
        if e < arr[midd]:
            maxIndex = midd - 1
        elif e > arr[midd]:
            minIndex = midd + 1
        elif midd < len(arr) and arr[midd] == e:
            return midd

    return -1


def binFind(arr, p):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == p else -1
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        midd = left + ((right-left) >> 1)
        if p < arr[midd]:
            right = midd - 1
        elif p > arr[midd]:
            left = midd + 1
        else:
            return midd
        
    return -1
        

if __name__ == '__main__':
    arr = [1, 4, 5, 6, 7, 9]
    res = binaryVal(arr, 6)
    res = binFind(arr, p=6)
    print(res)
