class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s.split() else len(s.split()[-1])
        
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail, res = len(s) - 1, 0
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            tail -= 1
            res += 1
        return res
        
