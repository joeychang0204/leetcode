class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {letter: i for i, letter in enumerate(order)}
        words = [[index[letter] for letter in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
