## 221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.   

<details><summary>sol</summary>
<p>

#### DP, time=O(mn), space=O(1). dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix[0]), len(matrix)
        for y in range(n):
            for x in range(m):
                matrix[y][x] = int(matrix[y][x])
                if matrix[y][x] and y and x:
                    matrix[y][x] = min(matrix[y-1][x], matrix[y][x-1], matrix[y-1][x-1]) + 1
                res = max(res, matrix[y][x] ** 2)
        return res

```
</p></details>

## 222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.  
Note:  
Definition of a complete binary tree from Wikipedia:  
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.  

<details><summary>sol</summary>
<p>

#### recursion, time=O(logn * logn), space=O(logn). For each root, check the height of left subtree and right. If have the same height -> ends at right subtree.

</p></details>

<details><summary>code</summary>
<p>

```python
def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(node):
            if not node:
                return -1
            return 1 + getHeight(node.left)
        if not root:
            return 0
        h = getHeight(root)
        if h == -1:
            return 0
        if getHeight(root.left) == getHeight(root.right):
            return 2**h + self.countNodes(root.right)
        else:
            return 2**(h-1) + self.countNodes(root.left)

```
</p></details>

## 223. Rectangle Area
Find the total area covered by two rectilinear rectangles in a 2D plane.  
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.  

<details><summary>sol</summary>
<p>

#### overlapped area = overlap_x * overlap_y. time=O(1), space=O(1). minRight-maxLeft, minTop-maxBottom

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec1 = abs((C-A) * (D-B))
        rec2 = abs((G-E) * (H-F))
        x_overlap = min(C, G) - max(A, E)
        y_overlap = min(D, H) - max(B, F)
        if x_overlap<=0 or y_overlap<=0:
            return rec1+rec2
        return rec1 + rec2 - (x_overlap * y_overlap)

```
</p></details>

## 224. 
description

<details><summary>sol</summary>
<p>

#### hint

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 225. Implement Stack using Queues
Implement the following operations of a stack using queues.  
push(x) -- Push element x onto stack.  
pop() -- Removes the element on top of the stack.  
top() -- Get the top element.  
empty() -- Return whether the stack is empty.  

<details><summary>sol</summary>
<p>

#### Use two queues. When popping, pop all of the elements except the last to the other queue. push : O(1), pop: time=O(n) space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.topElement = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.topElement = x
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        newStack = []
        while len(self.stack) > 1:
            self.topElement = self.stack.pop(0)
            newStack.append(self.topElement)
        tmp = self.stack[0]
        self.stack = newStack
        return tmp
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topElement
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

```
</p></details>

## 226. Invert Binary Tree
Invert a binary tree.  

<details><summary>sol1</summary>
<p>

#### recursive, time=O(n), space=O(h)=O(n) due to recursion

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # WA : root.left = self.invertTree(root.right), root.right = self.invertTree(root.left)
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.left, root.right = l, r
        return root
```
</p></details>

<details><summary>sol</summary>
<p>

#### iterative, time=O(n), space=O(n/2) = O(n) (last level worst case) 

</p></details>

<details><summary>code</summary>
<p>

```python
    def invertTree2(self, root):
        node = root
        queue = [node]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
```
</p></details>

## 227. Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.  
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.  

<details><summary>sol</summary>
<p>

#### use a stack to store the numbers, the operands will affect the stored number (ex. pushing -num for '-'). be careful with division of negative number. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i, ch in enumerate(s):
            if ch.isnumeric():
                num = num * 10 + int(ch)
            if ch in ['+', '-', '*', '/'] or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # notice : handle negative
                    # python3 version :
                    stack.append(int(stack.pop() / num))
                    # python2 version :
                    stack.append(int(stack.pop() / float(num)))
                sign = ch
                num = 0
        return sum(stack)
```
</p></details>

## 228. 
description

<details><summary>sol</summary>
<p>

#### hint

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.  
Note: The algorithm should run in linear time and in O(1) space.  

<details><summary>sol</summary>
<p>

#### [Boyer Moore Algorithm] (https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html). space=O(1), time=O(n). Idea : at most 2 candidates, first round find the candidates, second round validate their votes

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        cand1, cand2 = nums[0], nums[0]
        count1, count2 = 0, 0
        # find the majority candidates
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        res = []
        # validate candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        if count1 > len(nums) // 3:
            res.append(cand1)
        if count2 > len(nums) // 3:
            res.append(cand2)
        return res

```
</p></details>

## 230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.  
Note:  
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.  
Follow up:  
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?  

<details><summary>sol1</summary>
<p>

#### dfs - space=O(n), time=O(n). Return the sorted list in recursion.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # recursive, time=O(n), space=O(n)
        def dfs(node: TreeNode):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        return dfs(root)[k-1]
```
</p></details>

<details><summary>sol</summary>
<p>

#### bfs - space=O(h+k), time=O(h+k). While root, append to stack and go left. Pop last one as new root. Go to root's right for the next iteration. 

</p></details>

<details><summary>code</summary>
<p>

```python
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        # iterative, time=O(h+k), space=O(h+k)
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```
</p></details>
