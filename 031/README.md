## 31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.  
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).  
The replacement must be in-place and use only constant extra memory.  
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.  
1,2,3 → 1,3,2  
3,2,1 → 1,2,3  
1,1,5 → 1,5,1  
ex. 1, 2, 3, 5, 4, 1  

<details><summary>sol</summary>
<p>

#### from the tail, find the first ith element such that nums[i] < nums[i+1]. Swap it with the minimum one bigger than it (in this case, swapping 3 and 4). The remaining part of nums[i+1:] will be reversed sorted, just reverse it back. If it’s already reversed sorted, reverse it instead of sort it. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1, 2, 3, 5, 4, 1
        done = False
        if len(nums) < 2:
            return
        if nums:
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    bigger, pos = float('inf'), i
                    for j in range(i, len(nums)):
                        if nums[j] > nums[i]:
                            bigger = min(bigger, nums[j])
                            pos = j
                    nums[i], nums[pos] = bigger, nums[i]
                    nums[:] = nums[:i+1] + nums[i+1:][::-1]
                    done = True
                    break
        if not done:
            nums[:] = nums[::-1]
```
</p></details>

## 32. 
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

## 33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).  
You are given a target value to search. If found in the array return its index, otherwise return -1.  
You may assume no duplicate exists in the array.  
Your algorithm's runtime complexity must be in the order of O(log n).  

<details><summary>sol</summary>
<p>

#### use num[0] to check if target and nums[mid] is at the same side from pivot’s perspective. If so, cur = nums[mid]; else cur = infinity or -infinity. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            if (target < nums[0]) == (nums[mid] < nums[0]):
                cur = nums[mid]
            else:
                if target < nums[0]:
                    cur = -float('inf')
                else:
                    cur = float('inf')
            if cur > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
```
</p></details>

## 34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.  
Your algorithm's runtime complexity must be in the order of O(log n).  
If the target is not found in the array, return [-1, -1].

<details><summary>sol</summary>
<p>

#### do binary search twice. First find the left most. Finally, l is the answer. Apply the same method to find r again. l doesn’t need to be reset. time = O(logn), space = O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return res
        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return res
        res[0] = l
        r = len(nums) - 1
        while l < r:
            mid = int(l+r+1)/2
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        res[1] = r
        return res
```
</p></details>

## 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  
You may assume no duplicates in the array.  

<details><summary>sol</summary>
<p>

#### binary search, return left

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
```
</p></details>

## 36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:  
Each row must contain the digits 1-9 without repetition.  
Each column must contain the digits 1-9 without repetition.  
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.  

<details><summary>sol</summary>
<p>

#### use a list seen to record, (i, ch) (ch, j) and (i/3, j/3, ch).
finally use len(list) == len(set(list)) to check if there’s duplicate. time=O(n^2), space=O(n^2)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch != '.':
                    seen.append((i, ch))
                    seen.append((ch, j))
                    seen.append((int(i/3), int(j/3), ch))
        return len(seen) == len(set((seen)))

```
</p></details>

## 37. 
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

## 38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:  
1.     1  
2.     11  
3.     21  
4.     1211  
5.     111221  
1 is read off as "one 1" or 11.  
11 is read off as "two 1s" or 21.  
21 is read off as "one 2, then one 1" or 1211.  
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.  
Note: Each term of the sequence of integers will be represented as a string.  

<details><summary>sol</summary>
<p>

#### iterate and compare with the previous. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ['1']
        while len(ans) < 30:
            prev = ans[-1]
            counter, cur = 0, ''
            for i, ch in enumerate(prev):
                if i > 0 and prev[i] != prev[i-1]:
                    cur += str(counter) + prev[i-1]
                    counter = 0
                counter += 1
            cur += str(counter) + prev[-1]
            ans.append(cur)
        return ans[n-1]
                    

```
</p></details>

## 39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.  
The same repeated number may be chosen from candidates unlimited number of times.  

Note:  
All numbers (including target) will be positive integers.  
The solution set must not contain duplicate combinations.  

<details><summary>sol</summary>
<p>

####  remember to sort first. Use DFS (or backtracking) to solve this problem. time=O(candidates^target), space=O(target)???

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def backtrack(start, cur, val):
            if val == target:
                res.append(cur)
                return
            elif val > target:
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                backtrack(i, cur+[c], val+c)
        backtrack(0, [], 0)
                
        return res

```
</p></details>

## 40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.  
Each number in candidates may only be used once in the combination.  
Note:  
All numbers (including target) will be positive integers.  
The solution set must not contain duplicate combinations.

<details><summary>sol</summary>
<p>

#### Similar to 39, but start = i + 1. time=O(2^n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def backtrack(start, combination, val):
            if val > target:
                return
            elif val == target:
                if combination not in res:
                    res.append(combination)
                return
            for i in range(start, len(candidates)):
                backtrack(i+1, combination + [candidates[i]], val + candidates[i])
        backtrack(0, [], 0)
        return res
```
</p></details>
