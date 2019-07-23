class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        
        def expand(left: int, right: int):
            while  left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left, right = left-1, right+1
            return left+1, right-1
        
        for i, letter in enumerate(s):
            l, r = expand(i, i)
            if r - l > end - start:
                start, end = l, r
            l, r = expand(i-1, i)
            if r - l > end - start:
                start, end = l, r

        return s[start:end+1]
