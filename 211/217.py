class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0:
                if num == nums[i-1]:
                    return True
        return False
