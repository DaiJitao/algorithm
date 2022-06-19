def demo(arr):
    n = len(arr)
    if n < 3:
        return []
    
    if n == 3:
        return arr if sum(arr) == 0 else []
    
    arr = sorted(arr)
    
    dic = dict()
    for index, e in enumerate(arr):
        dic[e] = index
    
    res = []
    for i in range(n - 3):
        if arr[i] >= 0:
            return res
        
        for j in range(i + 1, n - 2):
            k = -(arr[i] + arr[j])
            if k in dic:
                inner = (arr[i], arr[j], k)
                res.append(arr)
                break
            else:
                break
    
    return res


def demo2(arr):
    n = len(arr)
    if n < 3:
        return []
    
    if n == 3:
        return arr if sum(arr) == 0 else []
    
    arr = sorted(arr)
    res = []
    for i in range(0, n - 1):
        if arr[i] > 0:
            break
        
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[left] + arr[i] + arr[right]
            if s == 0:
                res.append((arr[i], arr[left], arr[right]))
                while left < right and arr[left] == arr[left + 1]: left += 1
                while left < right and arr[right] == arr[right - 1]: right -= 1
                left += 1
                right -= 1
            elif s > 0:
                right -= 1
            elif s < 0:
                left += 1
    
    return res


if __name__ == '__main__':
    arr = [-3, -2, -1, 0, 1, 3, 3, 4]
    d = demo2(arr)
    print(d)
