class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] != t[i]:
                return False
            if ch not in d and t[i] in d.values():
                return False
            d[ch] = t[i]
        return True
    def isIsomorphic2(self, s, t):
        print(set(zip(s,t)))
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

print(Solution().isIsomorphic2("egg", "qqo"))
