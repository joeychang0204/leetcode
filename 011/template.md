## 11. Container with most water:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.  
Note: You may not slant the container and n is at least 2.  

<details><summary>sol</summary>
<p>

####  two pointer. We can discard the shorter one since all of the other pairs containing the shorter one don’t matter. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r-l) * min(height[l], height[r]) )
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        return res
```
</p></details>

## 12. Integer to Roman:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 
Symbol       Value  
I             1  
V             5  
X             10  
L             50  
C             100  
D             500  
M             1000  
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.  
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:  
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.  
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.  

<details><summary>sol</summary>
<p>

#### use list to save each digit. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def intToRoman(self, num):
        thousand = ['', 'M', 'MM', 'MMM']
        hundred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return thousand[num/1000] + hundred[(num%1000)/100] + ten[(num%100)/10]
```
</p></details>

## 13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.  
Symbol       Value  
I             1  
V             5  
X             10  
L             50  
C             100  
D             500  
M             1000  
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.  
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.  
There are six instances where subtraction is used:  
I can be placed before V (5) and X (10) to make 4 and 9.  
X can be placed before L (50) and C (100) to make 40 and 90.  
C can be placed before D (500) and M (1000) to make 400 and 900.  
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.  

<details><summary>sol</summary>
<p>

#### Nothing special, similar to 12. Can use dictionary instead. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, i = 0, 0
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        while i < len(s):
            if i < len(s)-1 and s[i] + s[i+1] in d:
                res += d[s[i] + s[i+1]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        return res
```
</p></details>

## 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string “".  

<details><summary>sol</summary>
<p>

#### find the shortest string, compare other string with it. If different, return. testcase : []    (empty). time=O(l*n) where l is the length of shortest string, space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]
        return shortest
```
</p></details>

## 15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.  
Note:  
The solution set must not contain duplicate triplets.  

<details><summary>sol</summary>
<p>

#### sort first. use ith element as the first number, perform 2Sum in its right. Repeating nums are annoying. Each i’th num has to compare with the previous one. time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        L = len(nums) - 1
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, L
            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l,r = l+1, r-1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                    while nums[r+1] == nums[r] and r > 0:
                        r -= 1
        return res

```
</p></details>

## Q
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

## Q
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

## Q
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

## Q
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

## Q
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
