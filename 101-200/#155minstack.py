class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = len(self.stack)
        self.stack = self.stack[0:tmp - 1]

    def top(self):
        """
        :rtype: int
        """
        topElement = self.stack[-1]
        return topElement

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
param_1 = obj.output()
print(param_1)
param_2 = obj.getMin()
print(param_2)
obj.pop()
param_3 = obj.output()
print(param_3)
param_4 = obj.getMin()
print(param_4)
obj.pop()
param_3 = obj.output()
print(param_3)
param_4 = obj.getMin()
print(param_4)
obj.pop()
param_3 = obj.output()
print(param_3)
param_4 = obj.getMin()
print(param_4)

