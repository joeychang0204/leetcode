class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        if not s:
            return []
        def dfs(word, part):
            if not word:
                self.res.append(part)
                return
            for i in range(1, len(word)+1):
                if word[:i] == word[:i][::-1]:
                    dfs(word[i:], part+[word[:i]])
        dfs(s, [])
        return self.res
