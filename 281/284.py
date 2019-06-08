class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.tmp = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp
        

    def next(self):
        """
        :rtype: int
        """
        res = self.tmp
        self.tmp = self.it.next() if self.it.hasNext() else None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.tmp is not None
