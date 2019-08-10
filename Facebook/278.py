class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            isBad = isBadVersion(mid)
            if isBad:
                r = mid
            else:
                l = mid + 1
        return l
