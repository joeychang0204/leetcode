class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = int((l+r)/2)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
        return target in matrix[mid]
        
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m * n - 1
        while l <= r:
            mid = int((l+r)/2)
            if target == matrix[mid/m][mid%m]:
                return True
            elif target < matrix[mid/m][mid%m]:
                r = mid - 1
            elif target > matrix[mid/m][mid%m]:
                l = mid + 1
        return False
        
