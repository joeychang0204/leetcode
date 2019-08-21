class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = collections.Counter(s[:len(p)])
        p_counter = collections.Counter(p)
        l, r = 0, len(p) - 1
        res = []
        while r < len(s):
            if s_counter == p_counter:
                res.append(l)
            l, r = l + 1, r + 1
            if r == len(s):
                break
            if s_counter[s[l-1]] == 1:
                # Counter can also pop by key
                s_counter.pop(s[l-1])
            else:
                s_counter[s[l-1]] -= 1
            # default value of Counter is 0, can += 1 directly
            s_counter[s[r]] += 1
        return res
            
