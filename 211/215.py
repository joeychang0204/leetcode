import random
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(l, r, pivot_index):
            pivot = nums[pivot_index]
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            smaller = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[smaller] = nums[smaller], nums[i]
                    smaller += 1
            nums[r], nums[smaller] = nums[smaller], nums[r]
            return smaller
        def select(l, r, target):
            # review1 : easy to forget
            
            if l == r:
                return nums[l]
            pivot_index = random.randrange(l, r)
            pivot_index = partition(l, r, pivot_index)
            print(l, r, pivot_index, nums)
            # review1 Runtime Error : remember to add return before calling select
            if pivot_index > target:
                return select(l, pivot_index-1, target)
            elif pivot_index < target:
                return select(pivot_index+1, r, target)
            else:
                return nums[pivot_index]
        res = select(0, len(nums)-1, len(nums)-k)
        return res
    def findKthLargest2(self, nums, k):
        # review 1 : forgot
        return heapq.nlargest(k, nums)[-1]
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
#print(Solution().findKthLargest2([3,3,3,3,3,3,3,3,3], 1))
