class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                new_s += letter
        return new_s == new_s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        return True
