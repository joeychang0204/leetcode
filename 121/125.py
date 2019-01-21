class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        news = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                news += s[i]
        return news == news[::-1]
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        head, tail = 0, len(s)-1
        while head <= tail:
            while head < len(s)-1 and not s[head].isalpha() and not s[head].isnumeric():
                head += 1
            while tail > 0 and not s[tail].isalpha() and not s[tail].isnumeric():
                tail -= 1
            
            if head <= tail and s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
        
