## 61. Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.

<details><summary>sol</summary>
<p>

#### traverse for length and find the tail, and then tail.next=head, shift tail for (length - k%length) times. case: k>length. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length = 1
        tail = ListNode(0)
        tail.next = head
        tail = tail.next
        while tail.next:
            length += 1
            tail = tail.next
        tail.next = head
        for i in range(length - k % length):
            tail = tail.next
        res = tail.next
        tail.next = None
        return res
```
</p></details>

## 62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).  
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).  
How many possible unique paths are there?  

<details><summary>sol</summary>
<p>

#### DP with one row. time=O(mn), space=O(m)

</p></details>

<details><summary>code</summary>
<p>

```python
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                l[j] += l[j-1]
        return l[-1]
```
</p></details>

## 63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).  
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).  
Now consider if some obstacles are added to the grids. How many unique paths would there be?  
An obstacle and empty space is marked as 1 and 0 respectively in the grid.  

<details><summary>sol</summary>
<p>

#### if we meet obstacle, dp[j] = 0. else same as 62. time=O(mn), space=O(m)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [0] * m
        dp[0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j-1]
        return dp[-1]

```
</p></details>

## 64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.  
Note: You can only move either down or right at any point in time.  

<details><summary>sol</summary>
<p>

#### easy DP. time=O(mn), space=O(m)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid[0]), len(grid)
        dp = [float('inf')] * m
        dp[0] = 0
        for i in range(n):
            for j in range(m):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]       
        return dp[-1]
```
</p></details>

## 65. 
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

## 66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.  
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.  
You may assume the integer does not contain any leading zero, except the number 0 itself.  

<details><summary>sol</summary>
<p>

#### Trivial using carry. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            carry = 1
            for i in range(len(digits)-1, -1, -1):
                digits[i] += carry
                if digits[i] >= 10:
                    digits[i] -= 10
                    carry = 1
                else:
                    carry = 0
                if carry == 0:
                    break
            if carry == 1:
                digits = [1] + digits
            return digits
```
</p></details>

## 67. Add Binary
Given two binary strings, return their sum (also a binary string).  
The input strings are both non-empty and contains only characters 1 or 0.  

<details><summary>sol</summary>
<p>

#### One liner using eval. time=O(1)? space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
```
</p></details>

## 68. 
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

## 69. Sqrt(x)
Implement int sqrt(int x).  
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.  
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.  

<details><summary>sol</summary>
<p>

#### binary search. time=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = int((l+r) / 2)
            if mid * mid > x:
                r = mid - 1
            else:
                if (mid+1) * (mid+1) > x:
                    return mid
                l = mid + 1
```
</p></details>

## 70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.  
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?  
Note: Given n will be a positive integer.

<details><summary>sol</summary>
<p>

#### simple dp using 2 variables. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        a, b = 1, 2
        cur = 3
        while cur <= n:
            a, b = b, a + b
            cur += 1
        return b
```
</p></details>
