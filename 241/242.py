class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(list(s)) == collections.Counter(list(t))
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
