from typing import List, Optional


def demo29(end, sub_divisor):
    """" 使用加法 """
    if sub_divisor == 1:
        return end

    count = 0
    t = 0
    while True:
        t += sub_divisor
        if t > end:
            break

        count += 1

    return count

if __name__ == '__main__':
    print(demo29(10, 2))


