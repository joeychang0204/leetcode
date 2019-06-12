## 101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).  
For example, this binary tree [1,2,2,3,4,4,3] is symmetric.

<details><summary>sol1</summary>
<p>

#### iterative with a stack. for each node, check if it's child's value is symmetric. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, childs = [root], []
        res = True
        while stack:
            childs = []
            while stack:
                cur = stack.pop(0)
                if cur:
                    childs.append(cur.left)
                    childs.append(cur.right)
            value = []
            for c in childs:
                if not c:
                    value.append(None)
                else:
                    value.append(c.val)
            if value != value[::-1]:
                res = False
                break
            stack = childs
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### recursively check left.left = right.right, left.right=right.left. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isSymmetric3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkLR(left, right):
            if left is None or right is None:
                return left is None and right is None
            return left.val == right.val and checkLR(left.left, right.right) and checkLR(left.right, right.left)
        
        if not root:
            return True
        return checkLR(root.left, root.right)
```
</p></details>

## 102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

<details><summary>sol1</summary>
<p>

#### iterative append each level to res. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack, child = [root], []
        res = []  
        while stack:
            child = []
            level = []
            while stack:
                cur = stack.pop(0)
                level.append(cur.val)
                if cur.left:
                    child.append(cur.left)
                if cur.right:
                    child.append(cur.right)
            res.append(level)
            stack = child
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### DFS with level. append new level if len(res) == level. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node, level):
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        return res
```
</p></details>

## 103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

<details><summary>sol</summary>
<p>

#### append the node value / add the node value in the front according to its level. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node, level):
            if not node:
                return
            if len(self.res) < level:
                self.res.append([node.val])
            else:
                if level % 2 == 1:
                    self.res[level-1].append(node.val)
                else:
                    self.res[level-1] = [node.val] + self.res[level-1]
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return self.res

```
</p></details>

## 104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.  
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  
  
Note: A leaf is a node with no children.  

<details><summary>sol1</summary>
<p>

#### DFS with level. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, level):
            if not node:
                return
            if level > self.res:
                self.res = level
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return self.res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### short recursive. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
```
</p></details>

## 105. Construct Binary Tree from Inorder and Preorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.  
  
Note:  
You may assume that duplicates do not exist in the tree.

<details><summary>sol</summary>
<p>

#### use preorder to find current root, separate inorder by the root, solve the problem recursively. time=O(n), space=??O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
```
</p></details>

## 106. Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.  
Note:  
You may assume that duplicates do not exist in the tree.  

<details><summary>sol</summary>
<p>

#### use preorder to find current root, separate inorder by the root, solve the problem recursively. time=O(n), space=??O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

```
</p></details>

## 107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

<details><summary>sol</summary>
<p>

#### bfs with level. reverse at last. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        level = 1
        while stack:
            tmp = []
            while stack:
                cur = stack.pop(0)
                if level > len(res):
                    res.append([cur.val])
                else:
                    res[level-1].append(cur.val)
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            stack = tmp
            level += 1
        return res[::-1]
```
</p></details>

## 108. Convert Sorted Array To Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.  
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

<details><summary>sol</summary>
<p>

#### use recursion, pick the middle of nums as root. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        i = int(len(nums)/2)
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root
```
</p></details>

## 109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.  
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

<details><summary>sol</summary>
<p>

#### solve recursively, use fast and slow to find the middle of linked list(should be slow). if slow == head (only one node in list) -> return root. time=O(nlogn), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def sortedListToBST2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        fast = slow = head
        prev = None #used for breaking list
        while fast and fast.next:
            fast=fast.next.next
            prev = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if slow == head:    #list has only one node
            return root
        root.right = self.sortedListToBST(slow.next)
        if prev:
            prev.next = None
        root.left = self.sortedListToBST(head)
        return root
```
</p></details>

## 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.  
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

<details><summary>sol</summary>
<p>

#### use recursion to get depth of each node. return -1 if unbalance. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def getDepth(node):
            if not node:
                return 0
            l = getDepth(node.left)
            r = getDepth(node.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l, r) + 1
        
        l = getDepth(root.left)
        r = getDepth(root.right)
        return abs(l-r) < 2 and l!=-1 and r != -1
```
</p></details>
