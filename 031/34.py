class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return res
        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return res
        res[0] = l
        r = len(nums) - 1
        while l < r:
            mid = int(l+r+1)/2
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        res[1] = r
        return res
                
        
