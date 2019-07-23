class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n^2) brute force, TLE
        res = 0
        for i, h in enumerate(height):
            leftMax, rightMax = 0, 0
            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])
            res += min(leftMax, rightMax) - h
        return res

    def trap2(self, height: List[int]) -> int:
        # DP with rightMax and leftMax lists
        res = 0
        if not height:
            return 0
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])
        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])
        
        
        for i, h in enumerate(height):
            res += min(leftMax[i], rightMax[i]) - h
        return res
