class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        if not matrix or not matrix[0]:
            return False
        def binarySearch(l):
            left, right = 0, len(l)-1
            while left <= right:
                mid = (left+right)//2
                if l[mid] == target:
                    return True
                elif l[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                res = binarySearch(row)
                if res:
                    return True
        return False
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(m+n) beautiful solution
        if not matrix or not matrix[0]:
            return False
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y <= len(matrix)-1:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            else:
                x -= 1
        return False
