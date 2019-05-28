class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        permutation = []
        counter = collections.Counter(s)
        mid = [k for k,v in counter.items() if v%2 == 1]
        if len(mid) > 1:
            return []
        def permute(cur):
            if len(cur) == len(s):
                permutation.append(cur)
                return
            for k,v in counter.items():
                if v >= 2:
                    counter[k] -= 2
                    permute(k + cur + k)
                    counter[k] += 2
        
        mid = mid[0] if len(mid) == 1 else ''
        permute(mid)
        return permutation
        
