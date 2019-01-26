class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        start = 0
        for i, ch in enumerate(str):
            if ch == " " or i == len(str)-1:
                l = start
                # don't reverse the spaces!!
                r = i-1 if ch==" " else i
                while l < r:
                    str[l], str[r] = str[r], str[l]
                    l, r = l+1, r-1
                start = i + 1
