
import math

def demo172(n):
    if n == 0:
        return 1
    if n == 1:
        return 0

    count = 0
    while n > 0:
        count += math.floor(n / 5)
        n = math.floor(n / 5)

    return count

if __name__ == '__main__':
    res = demo172(5)
    print(res)