class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1, 2, 3, 5, 4, 1
        done = False
        if len(nums) < 2:
            return
        if nums:
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    bigger, pos = float('inf'), i
                    for j in range(i, len(nums)):
                        if nums[j] > nums[i]:
                            bigger = min(bigger, nums[j])
                            pos = j
                    nums[i], nums[pos] = bigger, nums[i]
                    nums[:] = nums[:i+1] + nums[i+1:][::-1]
                    done = True
                    break
        if not done:
            nums[:] = nums[::-1]
