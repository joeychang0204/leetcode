class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # concise one-pass
        pos1, pos2 = -1, -1
        res = len(words)
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1-pos2))
        return res
