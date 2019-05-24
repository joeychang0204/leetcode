class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.topElement = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.topElement = x
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        newStack = []
        while len(self.stack) > 1:
            self.topElement = self.stack.pop(0)
            newStack.append(self.topElement)
        tmp = self.stack[0]
        self.stack = newStack
        return tmp
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topElement
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
