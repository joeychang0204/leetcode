class Solution(object):
    def permute(self, nums):
        res = []
        def backtrack(cur):
            if(len(cur) == len(nums)):
                res.append(cur)
                return
            for num in nums:
                if num not in cur:
                    backtrack(cur+[num])
        backtrack([])
        return res

    def permute2(self, nums):
        #iterative sol
        res = [[]]
        for num in nums:
            new_res = []
            for r in res:
                #be careful of this range
                for i in range(len(r)+1):
                    new_res.append(r[:i]+[num]+r[i:])
            res = new_res
        return res
        
