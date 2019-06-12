class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        for i, ch in enumerate(s):
            if ch == " " or i == len(s)-1:
                l = start
                r = i-1 if ch==" " else i
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l, r = l+1, r-1
                start = i + 1
