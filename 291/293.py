class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i, letter in enumerate(s):
            if letter == '+' and i > 0 and s[i-1] == '+':
                res.append(s[:i-1] + '--' + s[i+1:])
        return res
