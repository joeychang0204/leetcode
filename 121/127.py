class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def toDict(words):
            d = {}
            for word in words:
                for i, _ in enumerate(word):
                    cur = word[:i] + "_" + word[i+1:]
                    d[cur] = d.get(cur, []) + [word]
            return d
        d = toDict(wordList)
        q = [beginWord]
        used = set()
        res = 1
        while q:
            newq = []
            while q:  
                cur = q.pop(0)
                if cur == endWord:
                    return res
                if cur not in used:
                    used.add(cur)
                    for i, _ in enumerate(cur):
                        c = cur[:i] + "_" + cur[i+1:]
                        for word in d.get(c, []):
                            if word not in used:
                                newq.append(word)
            res += 1
            q = newq
        return 0
        
        
        
        
