import sys

sys.setrecursionlimit(100000)

def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)


def fib2(x: int):
    '''

    :param x:
    :return:
    '''
    if x < 0:
        return
    a = 1
    b = 1
    sums = [] * x
    for i in range(x):
        if i == 0 or i == 1:
            sums.append(1)
            continue
        sums.append(sums[-1] + sums[-2])

    return sums[-1]

def solution(ks=[], n=0):
    if n == 0 :
        return 0
    if ks == []:
        return -1



import time
start = time.time()
print(fib(10))
end1 = time.time()
print(fib2(1000))
end2 = time.time()
print("递归", end1-start)
print("递推", end2-end1)
