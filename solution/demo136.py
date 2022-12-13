

def singe_number(arr):

    if len(arr) == 0:
        return None

    if len(arr) <= 2:
        return None

    lst = [0] * 32
    for v in arr:
        bin_v = bin(v)[2:]

        for j, e in enumerate(bin_v[::-1]):
            index = 31 - j
            lst[index] += int(e)

    lst = [str(i % 2) for i in lst]
    return int(''.join(lst), 2)

if __name__ == '__main__':
    arr = [2, 2, 9, 9, 3, 3]
    res = singe_number(arr)
    print(res)