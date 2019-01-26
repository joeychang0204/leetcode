class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        res = []
        cur = ""
        l, r = 0, 9
        while r < len(s):
            cur = s[l:r+1]
            if cur in d:
                if d[cur] == 1:
                    res.append(cur)
                d[cur] += 1
            else:
                d[cur] = 1
            #Don't forget this ZZZ
            l, r = l+1, r+1
        return res
