class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if len(input) <= 3:
            return [eval(input)]
        res = []
        for i, num in enumerate(input):
            if num in '+-*/':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for r1 in res1:
                    for r2 in res2:
                        res.append(eval(str(r1) + num + str(r2)))
        return res
