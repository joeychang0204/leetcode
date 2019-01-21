class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = [1]
        for i in range(2, rowIndex+2):
            cur = []
            for j in range(i):
                if j-1 >= 0 and j < len(prev):
                    cur.append(prev[j-1] + prev[j])
                else:
                    cur.append(1)
            prev = cur
        return prev
