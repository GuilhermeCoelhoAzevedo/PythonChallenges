#https://neetcode.io/problems/minimum-stack

from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            val = min(self.minStack[-1], val)

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(3)
print(minStack.getMin()) # return 0
minStack.pop()
minStack.pop()
print(minStack.top())    # return 2
print(minStack.getMin()) # return 1