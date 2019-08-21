class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        req = collections.Counter(s2)
        s1_c = collections.defaultdict(int)
        l, r, cur = 0, 0, 0
        res = [float('inf'), 0, 0]
        while r < len(s1):
            added = s1[r]
            s1_c[added] += 1
            if added in req and s1_c[added] == req[added]:
                cur += 1
                
            while l <= r and cur == len(req):
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                prev = s1[l]
                s1_c[prev] -= 1
                if prev in req and s1_c[prev] == req[prev] - 1:
                    cur -= 1
                l += 1
            r += 1
        return s1[res[1]: res[2]+1] if res[0] != float('inf') else ''
