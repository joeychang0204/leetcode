class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        for i in range(len(s)-9):
            cur = s[i:i+10]
            repeated.add(cur) if cur in seen else seen.add(cur)
        return list(repeated)
