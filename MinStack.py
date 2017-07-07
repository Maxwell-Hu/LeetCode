class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stackMin = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.stackMin:
            self.stackMin.append(x)
        else:
            if x < self.stackMin[len(self.stackMin)-1]:
                self.stackMin.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.stackMin[len(self.stackMin)-1] and self.stack.count(x) == 0:
            self.stackMin.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stackMin[len(self.stackMin)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
