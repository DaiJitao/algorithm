def fun(n):
    if n <= 1:
        return 1
    else:
        return n * fun(n - 1)

if __name__ == '__main__':
    for i in range(30):
        res = fun(i)
        print(f"{i}={res}")
