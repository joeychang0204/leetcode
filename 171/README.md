## 171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.  
For example:  
A -> 1  
B -> 2  
C -> 3  
...  
Z -> 26  
AA -> 27  
AB -> 28  
…  

<details><summary>sol</summary>
<p>

#### res = res * 26 + ord difference. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = res * 26 + (ord(c) - ord('A') + 1)
        return res


```
</p></details>

## 172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

<details><summary>sol1</summary>
<p>

#### iterate the power of 5. res += n//(5 ** power). time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        power = 1
        while 5 ** power <= n:
            res += n//(5**power)
            power += 1
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### One liner using recursion. time=O(logn), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n//5 == 0 else n//5 + self.trailingZeroes(n//5)
```
</p></details>

## 173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.  
Calling next() will return the next smallest number in the BST.

<details><summary>sol</summary>
<p>

#### use a stack to store nodes, push all of the left nodes at once. In next, pop the last node and pushLeft(node.right). time=O(n) for n nodes, space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.pushLeft(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.nodes.pop(-1)
        val = node.val
        node = node.right
        self.pushLeft(node)
        return val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodes) >= 1
    def pushLeft(self, node):
        while node:
            self.nodes.append(node)
            node = node.left
```
</p></details>

## 174. 
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

## 175. 
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

## 176. 
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

## 177. 
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

## 178. 
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

## 179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

<details><summary>sol</summary>
<p>

#### define own cmp function and sort. time=O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cmp_function(a, b):
            return int(a+b) - int(b+a)
        nums = sorted(map(str, nums), cmp = cmp_function, reverse = True)
        #removing duplicate zeores
        res = ''.join(nums)
        if res[0] == '0':
            return '0'
        return res

```
</p></details>

## 180. 
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
