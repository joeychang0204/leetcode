class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        counter = collections.defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            counter[s[r]] += 1
            while len(counter) > k and l <= r:
                if counter[s[l]] == 1:
                    counter.pop(s[l])
                else:
                    counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
