class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        for i, r in enumerate(matrix):
            for j, element in enumerate(r):
                if element == 0:
                    row.append(i)
                    col.append(j)
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        
    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][0] == 0 or (j > 0 and matrix[0][j] == 0) or (col0 == 0 and j == 0):
                    matrix[i][j] = 0
        
print(Solution().setZeroes3(
[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]))
        
        
