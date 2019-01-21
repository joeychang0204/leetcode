class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = min(len(s), len(t))
        for i in range(l):
            if s[i] != t[i]:
                if len(s) > len(t):
                    return s[i+1:] == t[i:]
                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len(s) - len(t)) == 1
print(Solution().isOneEditDistance("a", "ac"))
