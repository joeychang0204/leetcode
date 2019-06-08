class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        # have to add 'list' in front of map for python3
        return list(map(words.index, words)) == list(map(pattern.find, pattern))
