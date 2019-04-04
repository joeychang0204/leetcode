class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or t < 0 or k<=0:
            return False
        # deal with negative nums, although no negative num in this test case
        smallest = min(nums)
        if smallest < 0:
            for i in range(len(nums)):
                nums[i] += (-smallest)
        buckets = {}
        for i, num in enumerate(nums):
            bucket_index = num // (t+1)
            if bucket_index in buckets:
                return True
            if (bucket_index+1) in buckets and abs(buckets[bucket_index+1] - num) <= t:
                return True
            if (bucket_index-1) in buckets and abs(buckets[bucket_index-1] - num) <= t:
                return True
            buckets[bucket_index]=num
            if (i+1) > k:
                buckets.pop(nums[i-k]//(t+1))
        return False
