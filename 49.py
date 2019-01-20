class Solution(object):
    #use the sorted words as key
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            cur = str(sorted((word)))
            prev = dic.get(cur, [])
            prev.append(word)
            dic[cur] = prev
        res = []
        for k, v in dic.items():
            res.append(v)
        return res

    #use the word's character count as key
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            dic[str(count)] = dic.get(str(count), []) + [word]
        res = []
        for k,v in dic.items():
            res.append(v)
        return res
