class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidates = ['00', '11', '88', '69', '96']
        res = []
        def backtrack(cur):
            if len(cur) == n:
                if n > 1 and cur[0] == '0':
                    return
                res.append(cur)
                return
            if len(cur) == 0 and n % 2 == 1:
                backtrack('1')
                backtrack('0')
                backtrack('8')
            else:
                for c in candidates:
                    backtrack(c[0] + cur + c[1])
        backtrack('')
        return res
                    
