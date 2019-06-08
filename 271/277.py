class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
