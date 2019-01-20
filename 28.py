class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        L = len(needle)
        for i in range(len(haystack)):
            if i + L - 1 > len(haystack) - 1:
                return -1
            if haystack[i:i+L] == needle:
                return i
        return -1
