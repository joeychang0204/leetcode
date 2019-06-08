class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = -float('inf')
        stack = []
        for p in preorder:
            if p < lower:
                return False
            while stack and stack[-1] < p:
                lower = stack.pop()
            stack.append(p)
        return True
    
    def verifyPreorder(self, preorder) -> bool:
        lower = -float('inf')
        stack_ptr = -1
        for i, p in enumerate(preorder):
            if p < lower:
                return False
            while stack_ptr >= 0 and p > preorder[stack_ptr]:
                lower = preorder[stack_ptr]
                stack_ptr -= 1
            stack_ptr += 1
            preorder[stack_ptr] = p
        return True
print(Solution().verifyPreorder([5,2,6,1,3]))
