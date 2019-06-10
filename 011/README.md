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

## 16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.  

<details><summary>sol</summary>
<p>

#### Using the means similar to 3Sum, nothing special. time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                cur = num + nums[l] + nums[r]
                if abs(cur - target) < abs(res - target):
                    res = cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return cur
        return res
```
</p></details>

## 17. Letter Combination of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.  
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.  

<details><summary>sol1</summary>
<p>

#### backtracking. time=O(3^N * 4^M) since some digits have 4 choices. space=O(3^N * 4^M) for solution.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = [['0'], ['0'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        if not digits:
            return []
        
        def backtracking(s, cur):
            if len(s) == len(digits):
                res.append(s)
                return
            for c in m[int(digits[cur])]:
                s = s + c
                backtracking(s, cur+1)
                s = s[:-1]
        backtracking('', 0)
        return res 
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iterative. time=O(3^N * 4^M) , space=O(3^N * 4^M) for solution.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = ['0', '0', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        all_combination = ['']
        if not digits:
            return []
        
        for digit in digits:
            cur_combination = []
            for letter in m[int(digit)]:
                for combination in all_combination:
                    cur_combination.append(combination + letter)
            all_combination = cur_combination
        return all_combination
```
</p></details>

## 18. 4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.  
Note:  
The solution set must not contain duplicate quadruplets.  
<details><summary>sol</summary>
<p>

#### Like 3 sum, but 2 for loops outside the final 2Sum. For N sum problems, we can solve it recursively and finally make it to 2Sum.  time=O(n^3), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        used = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i], nums[j]) in used:
                    continue
                cur = nums[i] + nums[j]
                l, r = j+1, len(nums)-1
                while l < r:
                    if cur + nums[l] + nums[r] < target:
                        l += 1
                    elif cur + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l, r = l+1, r-1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                used.add((nums[i], nums[j]))
        return res
```
</p></details>

## 19. Remove nth node from end of List
Given a linked list, remove the n-th node from the end of list and return its head.

<details><summary>sol</summary>
<p>

#### slow = fast = res = ListNode(0), res.next = head. fast move n+1 forward before slow move. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = slow = fast = ListNode(0)
        res.next = head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return res.next
```
</p></details>

## 20. Valid Parenthesis
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  
An input string is valid if:  
Open brackets must be closed by the same type of brackets.  
Open brackets must be closed in the correct order.  
Note that an empty string is also considered valid.  

<details><summary>sol</summary>
<p>

#### Use a stack, check the last element. test case : (  ,  ((,   ]. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i, ch in enumerate(s):
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not queue:
                    return False
                if (ch == '}' and stack[-1] != '{' ) or (ch == ']' and stack[-1] != '[' ) or (ch == ')' and stack[-1] != '(' ):
                    return False
                stack.pop(-1)
        if stack:
            return False
        return True

```
</p></details>
