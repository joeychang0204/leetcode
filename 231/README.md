## 231. Power of Two
Given an integer, write a function to determine if it is a power of two.   

<details><summary>sol</summary>
<p>

#### naive iterative, time=O(logn) /  if n is power of 2, n & (n-1) should be 0. time=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # time=O(logn)
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True
    def isPowerOfTwo2(self, n: int) -> bool:
        # time=O(1), space=O(1)
        return n > 0 and n & (n-1) == 0
```
</p></details>

## 232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.  
push(x) -- Push element x to the back of queue.  
pop() -- Removes the element from in front of queue.  
peek() -- Get the front element.  
empty() -- Return whether the queue is empty.  

<details><summary>sol</summary>
<p>

#### use 2 stacks. push elements into s1, pop from s2. when pop is called and s2 is empty, pop s1 into s2. push time=O(1), pop time=amortized O(1). 

</p></details>

<details><summary>code</summary>
<p>

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # first push to s1. when pop, pop all to s2
        self.s1 = []
        self.s2 = []
        self.front = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # push s1 to s2 if s2 is empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.s2) == 0:
            return self.front
        else:
            return self.s2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0

```
</p></details>

## 233. 
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

## 234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.  

<details><summary>sol</summary>
<p>

#### reverse the first half(fast&slow), and then compare. space=O(1), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool: 
        # O(1) space
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        slow, fast = rev, slow
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next
        return True

```
</p></details>

## 235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.  
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”  

<details><summary>sol</summary>
<p>

#### root should be between p and q, else recursively goto left or right. space=O(n), time=O(h).

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
```
</p></details>

<details><summary>sol</summary>
<p>

#### similar to sol1, but iterative. time=O(h), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative O(1) space
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
```
</p></details>

## 236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.  
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”  

<details><summary>sol1</summary>
<p>

#### recursively check left+right+porq>1. Note: True+True=2. Time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        def dfs(node):
            if not node:
                return False
            left, right = dfs(node.left), dfs(node.right)
            porq = (node.val==p.val or node.val==q.val)
            if left+right+porq > 1:
                self.res = node
            return left or right or porq
        dfs(root)
        return self.res
```
</p></details>

<details><summary>sol</summary>
<p>

#### iteratively maintain the parent pointer dictionary. The parent of root is None. space=O(n), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative
        parent = {root : None}
        stack = [root]
        while not (p in parent and q in parent):
            node = stack.pop(0)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        p_parents = []
        while p:
            p_parents.append(p)
            p = parent[p]
        while q:
            if q in p_parents:
                return q
            q = parent[q]
```
</p></details>

## 237. Delete Node in a Linked List
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.  

<details><summary>sol</summary>
<p>

#### PogChamp question, modify node's value and node.next directly.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # brain teaser question
        node.val, node.next = node.next.val, node.next.next

```
</p></details>

## 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].  

<details><summary>sol</summary>
<p>

#### use res to save the left product. multiply it with the right product during the second pass. extra space=O(1), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        # make res[i] = product of left elements of i
        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])
        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]
        return res

```
</p></details>

## 239. 
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

## 240. Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:  
Integers in each row are sorted in ascending from left to right.  
Integers in each column are sorted in ascending from top to bottom.  

<details><summary>sol</summary>
<p>

#### start from top-right, compare the element with target, move to left or bottom. time=O(m+n), space=O(1).

</p></details>

<details><summary>code</summary>
<p>

```python
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(m+n) beautiful solution
        if not matrix or not matrix[0]:
            return False
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y <= len(matrix)-1:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            else:
                x -= 1
        return False
```
</p></details>
