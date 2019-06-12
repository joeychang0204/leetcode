## 111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.  
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.  
Note: A leaf is a node with no children.

<details><summary>sol</summary>
<p>

#### dfs with depth, leaf -> left is None and right is None. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('inf')
        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)

        return self.res

```
</p></details>

## 112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.  
Note: A leaf is a node with no children.

<details><summary>sol</summary>
<p>

#### recursive. if leaf, check sum == root.val. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val
```
</p></details>

## 113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.  
Note: A leaf is a node with no children.

<details><summary>sol</summary>
<p>

#### dfs recording path, pass path+[node.val] in dfs call. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node, sum, path):
            if not node:
                return
            sum -= node.val
            #path.append(node.val) / path+=[node.val] Wrong Answer, will record all nodes
            if not node.left and not node.right and sum==0:
                self.res.append(path+[node.val])
            dfs(node.left, sum, path+[node.val])
            dfs(node.right, sum, path+[node.val])
        dfs(root, sum, [])
        return self.res
        

```
</p></details>

## 114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

<details><summary>sol</summary>
<p>

#### Godlike recursion. Use global variable self.prev to store the flattened right node. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

```
</p></details>

## 115. 
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

## 116. Populating Next Right Pointers in Each Node
Given a binary tree  
struct TreeLinkNode {  
TreeLinkNode *left;  
TreeLinkNode *right;  
TreeLinkNode *next;  
}  
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.  
Initially, all next pointers are set to NULL.  
  
Note:  
You may only use constant extra space.  
Recursive approach is fine, implicit stack space does not count as extra space for this problem.  
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

<details><summary>sol1</summary>
<p>

#### (go see the leetcode question)recursively : if has left, point it’s next to right. if has right, points its next to root’s next’s left. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next and root.next.left:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iterative, from top level to bottom level, keep moving to next and connect. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def connect2(self, root):
        if not root:
            return
        node = root
        while node:
            cur = node
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            node = node.left
```
</p></details>


## 117. Populating Next Right Pointers in Each Node II
Given a binary tree  
struct TreeLinkNode {  
TreeLinkNode *left;  
TreeLinkNode *right;  
TreeLinkNode *next;  
}  
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.  
Initially, all next pointers are set to NULL.  
  
Note:  
You may only use constant extra space.  
Recursive approach is fine, implicit stack space does not count as extra space for this problem.  

<details><summary>sol</summary>
<p>

#### iterative, similar to 116, handle more cases like some missing nodes in the middle. case : the first node in next level is not a left node(have to find the head of next level). time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        node = root
        while node:
            cur = node
            prev = None
            nxt = None
            while cur:
                if not nxt:
                    nxt = cur.left if cur.left else cur.right
                if cur.left and cur.right:
                    cur.left.next = cur.right
                if prev:
                    if cur.left:
                        prev.next = cur.left
                    elif cur.right:
                        prev.next = cur.right
                if cur.right:
                    prev = cur.right
                elif cur.left:
                    prev = cur.left
                cur = cur.next
            node = nxt

```
</p></details>

## 118. Pascal’s Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

<details><summary>sol</summary>
<p>

#### check j-1 >= 0 and j < len(prev). time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(2, numRows+1):
            cur = []
            prev = res[-1]
            for j in range(i):
                if j-1 >= 0 and j < len(prev):
                    cur.append(prev[j-1] + prev[j])
                else:
                    cur.append(1)
            res.append(cur)
        return res
```
</p></details>

## 119. Pascal’s Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.  
  
Note that the row index starts from 0.  

<details><summary>sol</summary>
<p>

#### similar to 118. start from index, should end at rowIndex + 1. time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = [1]
        for i in range(2, rowIndex+2):
            cur = []
            for j in range(i):
                if j-1 >= 0 and j < len(prev):
                    cur.append(prev[j-1] + prev[j])
                else:
                    cur.append(1)
            prev = cur
        return prev

```
</p></details>

## 120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

<details><summary>sol</summary>
<p>

#### simple dp, for each index j, check if j-1 and j in previous row is valid. time=O(n^2), space=O(n) where n is the edge length of the triangle.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = triangle[0]
        for i in range(1, len(triangle[-1])):
            cur = triangle[i]
            for j, e in enumerate(cur):
                if j-1 >= 0 and j < len(dp):
                    cur[j] += min(dp[j-1], dp[j])
                elif j < len(dp):
                    cur[j] += dp[j]
                elif j-1 >= 0:
                    cur[j] += dp[j-1]
            dp = cur
        return min(dp)

```
</p></details>
