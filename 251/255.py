class Solution:
    def verifyPreorder(self, preorder) -> bool:
        if len(preorder) <=1:
            return True
        for i, num in enumerate(preorder):
            if num > preorder[0] or i == len(preorder)-1:
                print(preorder)
                print(all(preorder[j] < preorder[0] for j in range(1, i)))
                print(all(preorder[j] > preorder[0] for j in range(i,len(preorder))))
                if not all(preorder[j] < preorder[0] for j in range(1, i)) or not all(preorder[j] > preorder[0] for j in range(i,len(preorder))):
                    return False
                return self.verifyPreorder(preorder[1:i]) and self.verifyPreorder(preorder[i:])

print(Solution().verifyPreorder([5,2,1,3,6]))
