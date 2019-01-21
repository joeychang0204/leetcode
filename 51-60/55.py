class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        cur = 0
        i = 0
        while cur < len(nums):
            if cur == i and nums[i] == 0:
                break
            cur = max((cur, i + nums[i]))
            i += 1
        return cur >= len(nums) - 1
