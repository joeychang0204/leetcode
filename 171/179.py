class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cmp_function(a, b):
            return int(a+b) - int(b+a)
        nums = sorted(map(str, nums), cmp = cmp_function, reverse = True)
        #removing duplicate zeores
        res = ''.join(nums)
        if res[0] == '0':
            return '0'
        return res
