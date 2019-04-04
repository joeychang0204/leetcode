class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i, num in enumerate(nums):
            if num in s:
                return True
            s.add(num)
            if len(s) > k:
                s.remove(nums[i-k]) 
        return False
