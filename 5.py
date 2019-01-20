class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            j = 1
            cur = s[i]
            while i-j >= 0 and i+j < len(s):
                if s[i-j] == s[i+j]:
                    cur = s[i-j] + cur + s[i+j]
                    j += 1
                else:
                    break
            if len(cur) > len(res):
                res = cur
            if i < len(s) - 1 and s[i] == s[i+1]:
                j = 1
                cur = s[i] + s[i]
                while i-j >= 0 and i+1+j < len(s):
                    if s[i-j] == s[i+1+j]:
                        cur = s[i-j] + cur + s[i-j]
                        j += 1
                    else:
                        break
            if len(cur) > len(res):
                res = cur
        return res
            
