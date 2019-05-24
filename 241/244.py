class WordDistance:

    def __init__(self, words: List[str]):
        self.words = words
        self.index = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.index[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = len(self.words)
        i, j = 0, 0
        while i < len(self.index[word1]) and j < len(self.index[word2]):
            index1, index2 = self.index[word1][i], self.index[word2][j]
            res = min(res, abs(index1-index2))
            if index1 < index2:
                i += 1
            else:
                j += 1
        return res
