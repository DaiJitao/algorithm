

def fn(n):
    if n == 1:
        return n
    else:
        return n * fn(n-1)


def demo172():
    pass

if __name__ == '__main__':
    for i in range(1, 40+1):
        n = i
        res = fn(n)
        print(f"{i}:{res}")