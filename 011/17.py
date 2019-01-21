# backtracking:
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = [['0'], ['0'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        if not digits:
            return []
        
        def backtracking(s, cur):
            if len(s) == len(digits):
                res.append(s)
                return
            for c in m[int(digits[cur])]:
                s = s + c
                backtracking(s, cur+1)
                s = s[:-1]
        backtracking('', 0)
        return res    
        

# iterative
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = ['0', '0', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        all_combination = ['']
        if not digits:
            return []
        
        for digit in digits:
            cur_combination = []
            for letter in m[int(digit)]:
                for combination in all_combination:
                    cur_combination.append(combination + letter)
            all_combination = cur_combination
        return all_combination
        
