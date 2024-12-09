from typing import List, Optional
import numpy as np

def demo(travels, trytime):
    count = 1
    flag = True
    start_index = 0
    n = len(travels)

    temp = []
    isPlay = True
    for i in range(trytime):
        while flag:
            stepsize = np.random.randn(1, 6)
            count += 1
            conver = start_index + stepsize
            if conver > n-1:
                flag = False

            else:
                res = travels[conver]
                if res == 0:
                    continue
                elif res > 0:

                    conver = conver + res
                elif res < 0:
                    conver = conver + res


        temp.append(count)

    return  sum(temp)/trytime




