class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common()[0][0]
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter , candidate = 0, None
        for num in nums:
            if counter == 0:
                candidate = num
            if candidate == num:
                counter += 1
            else:
                counter -= 1
        return candidate
