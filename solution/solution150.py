from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ch = {'/', '+', '-', '*'}
        if len(tokens) == 1:
            res = int(tokens[0])

        stack = []

        for i in tokens:
            if i in ch:
                p1 = stack.pop()
                p2 = stack.pop()
                if i == '+':
                    res = p2 + p1
                elif i == '/':
                    res = int(p2 / p1)
                elif i == '-':
                    res = p2 - p1
                elif i == '*':
                    res = p2 * p1

                stack.append(res)
            else:
                i = int(i)
                stack.append(i)

        return res

if __name__ == '__main__':
    t = ["18"]
    res = Solution().evalRPN(t)
    print(res)