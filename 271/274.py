class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        for h in range(len(citations), 0, -1):
            if citations[len(citations)-h] >= h:
                return h
        return 0
    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        count = [0] * (n+1)
        for citation in citations:
            count[min(n, citation)] += 1
        cur = 0
        for h in range(n, -1, -1):
            cur += count[h]
            if cur >= h:
                return h
        return 0
