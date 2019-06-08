class ZigzagIterator(object):
    # use lists too suck, try use iterator!
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [(len(v), iter(v)) for v in v1, v2 if v]

    def next(self):
        """
        :rtype: int
        """
        length, it = self.data.pop(0)
        res = next(it)
        if length-1 > 0:
            self.data.append((length-1, it))
        return res
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)
