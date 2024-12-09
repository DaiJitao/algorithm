from typing import List, Optional


class Solution:
    def reverse(self, x: int) -> int:
        minp = '-2147483648'
        maxp = '2147483647'

        tmp = str(x)
        if tmp[0] == '-':
            if len(tmp[1:]) > len(minp) - 1:
                return 0
            elif len(tmp[1:]) == len(minp) - 1:
                newInt = tmp[1:][::-1]
                for i, newInt_j in zip(minp[1:], newInt):
                    if int(newInt_j) > int(i):
                        return 0

                return -newInt
            return -tmp[1:][::-1]
        else:
            pass


