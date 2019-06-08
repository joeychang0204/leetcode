class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        l, r = 0, length-1
        while l <= r:
            mid = (l+r) // 2
            if citations[mid] < length - mid:
                l = mid + 1
            elif citations[mid] > length - mid:
                r = mid - 1
            else:
                return citations[mid]
        return length - l
