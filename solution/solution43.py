# encoding=utf8
import sys

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
            return None
        
        sump = 0
        for index, i in enumerate(num1[::-1]):
            v = int(i)
            p = v * int(num2) * (10 ** index)
            sump += p
            
        return str(sump)
    
if __name__ == '__main__':
    num1 = '29'
    num2 = '33'
    res = Solution().multiply(num1, num2)
    print(res)
    print(int(num1) * int(num2))