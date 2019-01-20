class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            if (target < nums[0]) == (nums[mid] < nums[0]):
                cur = nums[mid]
            else:
                if target < nums[0]:
                    cur = -float('inf')
                else:
                    cur = float('inf')
            if cur > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: #first half is ordered
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]: #second half is ordered
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
