## 71. Simplify Path
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.  
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix  
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.  

<details><summary>sol</summary>
<p>

#### use stack to store the directories. check if empty when trying to pop. return ‘/‘ if final stack is empty. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for d in dirs:
            if d == '..' and stack:
                stack.pop()
            elif d != '.' and d != '..' and d:
                stack.append(d)
        return '/' + '/'.join(stack)
```
</p></details>

## 72. 
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

## 73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.  

<details><summary>sol</summary>
<p>

#### modify matrix[0][i] = 0 if column i should be 0, matrix[i][0] = 0 if row should be 0. since row0 and column0 may use the same cell, need a variable col0. time=O(mn), space=O(1)
</p></details>

<details><summary>code</summary>
<p>

```python
    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][0] == 0 or (j > 0 and matrix[0][j] == 0) or (col0 == 0 and j == 0):
                    matrix[i][j] = 0
```
</p></details>

## 74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:  
Integers in each row are sorted from left to right.  
The first integer of each row is greater than the last integer of the previous row.

<details><summary>sol</summary>
<p>

#### r = m*n-1, compare matrix[mid/n][mid%n] with target. time=O(logmn), space=O(1)

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
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m * n - 1
        while l <= r:
            mid = int((l+r)/2)
            if target == matrix[mid/m][mid%m]:
                return True
            elif target < matrix[mid/m][mid%m]:
                r = mid - 1
            elif target > matrix[mid/m][mid%m]:
                l = mid + 1
        return False
```
</p></details>

## 75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.  
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.  
Note: You are not suppose to use the library's sort function for this problem.  
<details><summary>sol</summary>
<p>

#### move 0 to left, move 2 to right. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, cur, p2 = 0, 0, len(nums)-1
        while cur <= p2:
            if nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            elif nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            else:
                cur += 1
```
</p></details>

## 76. 
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

## 77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

<details><summary>sol</summary>
<p>

#### backtracking, use start, don’t use remains. remains will lead to TLE. time=O(k*C(n, k)). space=O(C(n, k))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        def backtrack(curr, l, start):
            if l == k:
                self.res.append(curr)
                return
            for r in range(start, n+1):
                if not curr or (curr and r > curr[-1]):
                    backtrack(curr+[r], l+1, start + 1)
        backtrack([], 0, 1)
        return self.res
```
</p></details>

## 78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).  
Note: The solution set must not contain duplicate subsets.

<details><summary>sol</summary>
<p>

#### backtracking, next start should be i+1. time=O(2^n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def backtrack(curr, start):
            self.res.append(curr)
            for i in range(start, len(nums)):
                backtrack(curr+[nums[i]], i+1)
        backtrack([], 0)
        return self.res
```
</p></details>

## 79. Word Search
Given a 2D board and a word, find if the word exists in the grid.  
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

<details><summary>sol</summary>
<p>

#### DFS. time=O(n*m*len(word)), space=O(mn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board[0]), len(board)
        used = [[False]* r for i in range(c)]
        def search(row, col, remains):
            if not remains:
                return True
            if row < 0 or row > c-1 or col < 0 or col > r-1:
                return False
            if used[row][col] or board[row][col] != remains[0]:
                return False
            used[row][col] = True
            res = search(row-1, col, remains[1:]) or search(row+1, col, remains[1:]) or search(row, col-1, remains[1:]) or search(row, col+1, remains[1:])
            used[row][col] = False
            return res
        for i in range(c):
            for j in range(r):
                if search(i, j, word):
                    return True
        return False
```
</p></details>

## 80. Remove duplicates from sorted array II
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.  
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

<details><summary>sol</summary>
<p>

#### Use a pointer res start from 0, compare num and nums[res-2]. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if res < 2 or nums[res-2] != num:
                nums[res] = num
                res += 1
        return res
```
</p></details>
