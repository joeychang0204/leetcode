class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = [0] * 128
        for letter in s:
            counter[ord(letter)] = 1 - counter[ord(letter)]
        return sum(counter) <= 1
