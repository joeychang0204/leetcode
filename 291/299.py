class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = collections.defaultdict(int)
        A, B = 0, 0
        for i, s in enumerate(secret):
            g = guess[i]
            if g == s:
                A += 1
            else:
                if count[g] < 0:
                    B += 1
                if count[s] > 0:
                    B += 1
                count[g] += 1
                count[s] -= 1
        return str(A) + 'A' + str(B) + 'B'
