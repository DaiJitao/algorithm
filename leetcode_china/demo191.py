

def demo(n):
    if n == 0:
        return 0

    count = 0
    while n:
        count += 1
        n &= (n-1)

    return count



if __name__ == '__main__':
    r = demo(89)
    print(r)