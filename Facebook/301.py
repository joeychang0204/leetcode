class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()
        self.minRemoved = float('inf')
        def backtrack(cur_s, index, leftCount, rightCount, removed):
            if index == len(s):
                if leftCount == rightCount:
                    if removed < self.minRemoved:
                        self.res = set()
                        self.res.add(cur_s)
                        self.minRemoved = removed
                    elif removed == self.minRemoved:
                        self.res.add(cur_s)
                return
            if rightCount > leftCount or removed > self.minRemoved:
                return
            if s[index] not in '()':
                backtrack(cur_s + s[index], index+1, leftCount, rightCount, removed)
            elif s[index] == '(':
                backtrack(cur_s + s[index], index+1, leftCount+1, rightCount, removed)
                backtrack(cur_s , index+1, leftCount, rightCount, removed+1)
            else:
                backtrack(cur_s + s[index], index+1, leftCount, rightCount+1, removed)
                backtrack(cur_s , index+1, leftCount, rightCount, removed+1)
        backtrack('', 0, 0, 0, 0)
        return list(self.res)

    def removeInvalidParentheses2(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            leftCounter, rightCounter = 0, 0
            for letter in s:
                if letter == '(':
                    leftCounter += 1
                elif letter == ')':
                    rightCounter += 1
                    if rightCounter > leftCounter:
                        return False
            return leftCounter == rightCounter
        combinations = {s}
        while combinations:
            sol = list(filter(isValid, combinations))
            if sol:
                return sol
            combinations = {c[:i] + c[i+1:] for c in combinations for i in range(len(c))}
        return []
