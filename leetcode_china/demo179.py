import functools


def demo179(nums):
    pnums = map(str, nums)

    def cmp(a, b):
        if a + b > b + a:
            return 1
        elif a + b < b + a:
            return -1
        return 0

    strs = sorted(pnums, key=functools.cmp_to_key(cmp), reverse=True)
    return ''.join(strs)


if __name__ == '__main__':
    nums = [12, 23, 86, 9]
    nums = demo179(nums)
    print(nums)
