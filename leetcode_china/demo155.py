from typing import List


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)

        else:

            self.stack.append(val)
            size = len(self.stack)
            for index in range(size - 1, 0, -1):
                if self.stack[index] > self.stack[index - 1]:
                    self.stack[index], self.stack[index - 1] = self.stack[index - 1], self.stack[index]

                else:
                    break

    def pop(self) -> None:
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.top()


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
