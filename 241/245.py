class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = -1, -1
        res = len(words)
        for i, word in enumerate(words):
            if word == word1 and word1 == word2:
                if pos1 <= pos2:
                    pos1 = i
                else:
                    pos2 = i
            elif word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1-pos2))
        return res
