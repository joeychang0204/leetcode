class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, l, start = 0, 0, 0
        last = {}
        for i, c in enumerate(s):
            if c not in last or last[c] < start:
                l += 1
            else:          
                l = i - last[c]
                start = last[c] + 1
            last[c] = i
            res = max(res, l)
        return res
                
            
