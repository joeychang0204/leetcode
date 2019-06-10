## 51. 
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

## 52. 
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

## 53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

<details><summary>sol</summary>
<p>

####  two variables. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best, cur = nums[0], 0
        for num in nums:
            cur = max(cur+num, num)
            best = max(best, cur)
        return best
```
</p></details>

## 54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

<details><summary>sol</summary>
<p>

#### to change direction: dx, dy = dy, -dx. clear matrix[y][x] after appending to res, so we know it’s visited. time=O(m*n), space=O(m*n) for result.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []
        while len(res) < m*n:
            res.append(matrix[y][x])
            matrix[y][x] = ''
            if  (x+dx) % n != x+dx or (y+dy)%m != y+dy or matrix[y+dy][x+dx] == '':
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return res
```
</p></details>

## 55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.  
Each element in the array represents your maximum jump length at that position.  
Determine if you are able to reach the last index.  

<details><summary>sol</summary>
<p>

#### cur = max(cur, i+nums[i]). break condition : cur == i and nums[i] == 0. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        cur = 0
        i = 0
        while cur < len(nums):
            if cur == i and nums[i] == 0:
                break
            cur = max((cur, i + nums[i]))
            i += 1
        return cur >= len(nums) - 1
```
</p></details>

## 56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

<details><summary>sol</summary>
<p>

#### sort first. compare res[-1].end and interval.start. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda x : x.start)
        res = []
        for i, interval in enumerate(intervals):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        return res
```
</p></details>

## 57. 
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

## 58. Length of Last word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  
If the last word does not exist, return 0.  
Note: A word is defined as a character sequence consists of non-space characters only.  

<details><summary>sol</summary>
<p>

#### cheating one-liner using split / start from tail, skip the spaces and then count.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s.split() else len(s.split()[-1])
        
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail, res = len(s) - 1, 0
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            tail -= 1
            res += 1
        return res
```
</p></details>

## 59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.  

<details><summary>sol</summary>
<p>

#### similar to 54. If the next res element != 0, then we should make a turn. time=O(n^2), space=O(n^2)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        x, y, dx, dy = 0, 0, 1, 0
        res = [[0] * n for i in range(n)]
        cur = 1
        while cur <= n * n:
            res[y][x] = cur
            cur += 1
            if res[(y+dy)%n][(x+dx)%n] != 0:
                dx, dy = -dy, dx
            x, y = x+dx, y+dy
        return res

```
</p></details>

## 60. Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:  
"123", "132", "213", "231", "312", "321"  
Given n and k, return the kth permutation sequence.  
Note:  
Given n will be between 1 and 9 inclusive.  
Given k will be between 1 and n! inclusive.  

<details><summary>sol</summary>
<p>

#### Use a list to store 1! to n!. each permutation (from 1234 to 2134) will cost n!(3!). time=O(n!), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [i for i in range(n+1)]
        remain = [i for i in range(1, n+1)]
        for i in range(3, n+1):
            fac[i] = i * fac[i-1]
        fac[0] = 1
        print(fac)
        cur = 0
        res = ''
        while len(res) < n:
            f = fac[len(remain) - 1]
            for num in remain:
                if cur + f < k:
                    cur += f
                elif cur + f >= k:
                    res += str(num)
                    remain.remove(num)
                    break
        return res
```
</p></details>
