class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r-l) * min(height[l], height[r]) )
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        return res
