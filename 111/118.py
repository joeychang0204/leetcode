class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(2, numRows+1):
            cur = []
            prev = res[-1]
            for j in range(i):
                if j-1 >= 0 and j < len(prev):
                    cur.append(prev[j-1] + prev[j])
                else:
                    cur.append(1)
            res.append(cur)
        return res
