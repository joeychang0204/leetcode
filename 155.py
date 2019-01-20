class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min = min(self.min, x)

    def pop(self):
        """
        :rtype: void
        """
        cur = self.stack.pop(-1)
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = float('inf')

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        print(self.stack)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop(-1) == self.min:
            self.min = self.stack.pop(-1)
        print(self.stack)

    def top(self):
        """
        :rtype: int
        """
        print("top=== "+str(self.stack[-1]))
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        print("min === " + str(self.min))
        return self.min

class MinStack3(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x-self.min)
            if x < self.min:
                self.min = x
    def pop(self):
        """
        :rtype: void
        """
        cur = self.stack.pop(-1)
        if cur < 0:
            self.min = self.min - cur

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        if top > 0:
            return int(top + self.min)
        else:
            return int(self.min)
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
s = MinStack2()
s.push(2)
s.push(1)
s.push(3)
s.push(0)
s.push(-5)
s.top()
s.pop()
s.getMin()
s.pop()
s.getMin()
s.pop()
s.push(4)
s.top()
s.getMin()
