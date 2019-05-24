class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # first push to s1. when pop, pop all to s2
        self.s1 = []
        self.s2 = []
        self.front = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # push s1 to s2 if s2 is empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.s2) == 0:
            return self.front
        else:
            return self.s2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0
