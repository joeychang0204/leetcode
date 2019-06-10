## 91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:  
'A' -> 1  
'B' -> 2  
...
'Z' -> 26  
Given a non-empty string containing only digits, determine the total number of ways to decode it.

<details><summary>sol</summary>
<p>

#### dp. each time check 2 consecutive digits. case : start with 0. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        dp[0], dp[1] = 1, 1
        for j in range(2, len(s)+1):
            i = j - 1
            num = int(s[i-1] + s[i])
            if s[i] == '0' and s[i-1] not in ['1', '2']:
                return 0
            elif num == 10 or num == 20:
                dp[j] = dp[j-2]
            elif 11 <= num <= 26:
                dp[j] = dp[j-1] + dp[j-2]
            else:   #like 27, 39
                dp[j] = dp[j-1]
        return dp[-1]
```
</p></details>

## 92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.  
Note: 1 ≤ m ≤ n ≤ length of list.

<details><summary>sol</summary>
<p>

#### modifying next pointers. 1-2-3-4-5 -> 1-3-2-4-5 -> 1-4-3-2-5. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = prev = ListNode(0)
        dummy.next = head
        cur = 1
        while cur < m:
            prev = head
            head = head.next
            cur += 1
        #1-2-3-4-5
        #1-3-2-4-5
        #1-4-3-2-5
        for i in range(n-m):
            curr = head.next #3, 4
            nxt = curr.next #4, 5
            head.next = nxt #2-4, 2-5
            curr.next = prev.next   #3-2, 
            prev.next = curr    #1-3, 1-4      
        
        return dummy.next
```
</p></details>

## 93. Restore IP Address
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

<details><summary>sol1</summary>
<p>

#### brute force : i, j, k. check each int and remaining length. case : 010.1.1.1(any num start from 0 is invalid). time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(1,4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    n1, n2, n3, n4 = s[:i],s[i:j], s[j:k], s[k:]
                    inValid = False
                    for n in [n1, n2, n3, n4]:
                        if not n or (n[0] == '0' and len(n) > 1):
                            inValid = True
                            break
                    if inValid:
                        continue
                            
                    if int(n1)<=255 and int(n2)<=255 and int(n3)<=255 and int(n4) <= 255:
                        res.append(n1+'.'+n2+'.'+n3+'.'+n4)
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### dfs. dfs deeper if the length of remain is valid. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        def dfs(seperated, remain, cur):
            if seperated == 4:
                if not remain:
                    # remove the last dot
                    self.res.append(cur[:-1])
                return
            if len(remain) >= 1:
                dfs(seperated+1, remain[1:], cur + remain[:1] + '.')
            if len(remain) >= 2 and remain[0] != '0':
                dfs(seperated+1, remain[2:], cur + remain[:2] + '.')
            if len(remain) >= 3 and remain[0] != '0' and int(remain[:3]) <= 255:
                dfs(seperated+1, remain[3:], cur + remain[:3] + '.')
        dfs(0, s, '')
        return self.res
                
```
</p></details>

## 94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

<details><summary>sol</summary>
<p>

#### iterative : while root: root = root.left. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            while root:
                stack = [root] + stack
                root = root.left
            root = stack.pop(0)
            res.append(root.val)
            root = root.right
        return res
```
</p></details>

## 95. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

<details><summary>sol</summary>
<p>

#### recursive, pick root in range(start, end+1), and pick left and right from recursive list. time=space=O((4^n) / (n^0.5))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n == 0:
            return []
        def genTree(start, end):
            list = []
            if start > end:
                return [None]
            for i in range(start, end+1):
                l_list = genTree(start, i-1)
                r_list = genTree(i+1, end)
                for l in l_list:
                    for r in r_list:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        list.append(root)
            return list
        return genTree(1, n)
```
</p></details>

## 96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

<details><summary>sol1</summary>
<p>

#### only recursion will TLE. store the result to save time. time?? space??

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [0] * (n+1)
        def genTree(start, end):
            res = 0
            if start > end:
                return 1
            for i in range(start, end+1):
                if self.dp[i-1-start] == 0:
                    l_num = genTree(start, i-1)
                else:
                    l_num = self.dp[i-1-start]
                if self.dp[end-i-1] == 0:
                    r_num = genTree(i+1, end)
                else:
                    r_num = self.dp[end-i-1]
                res += l_num * r_num
            self.dp[end-start] = res
            return res
        return genTree(1, n)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### PogChamp dp. dp[i] = sigma(dp[j-1] * dp[i-j]). time=O(n^2), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            cur = 0
            for j in range(1, i+1):
                cur += dp[j-1] * dp[i-j]
            dp[i] = cur
        return dp[n]
```
</p></details>

## 97. 
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

## 98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).  
Assume a BST is defined as follows:  
The left subtree of a node contains only nodes with keys less than the node's key.  
The right subtree of a node contains only nodes with keys greater than the node's key.  
Both the left and right subtrees must also be binary search trees.

<details><summary>sol</summary>
<p>

#### in order traversal of BST should output a sorted array of nums. case : duplicate nums such as [1,1], should return false. recursive/ iterative. time=O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        dfs(root)
        return len(self.res) == len(set(self.res)) and self.res == sorted(self.res)
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #iterative
        res = []
        stack = []
        while root or stack:
            while root:
                stack = [root] + stack
                root = root.left
            root = stack.pop(0)
            res.append(root.val)
            root = root.right
        return len(res) == len(set(res)) and res == sorted(res)
```
</p></details>

## 99. 
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

## 100. Same Tree
Given two binary trees, write a function to check if they are the same or not.  
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

<details><summary>sol</summary>
<p>

#### recursively check. time=O(n), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return (p is None) == (q is None)
```
</p></details>
