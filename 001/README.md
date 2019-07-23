## 1. 2 Sum: 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  

<details><summary>sol</summary>
<p>

#### Use dictionary. time=O(n), space=O(n)   ps: O(1) amortized lookup time since dict is implemented with hash table

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = dict()
        for i in range(len(nums)):
            if target - nums[i] in numsDict:
                return [numsDict[target - nums[i]], i]
            else:
                numsDict[nums[i]] = i
```
</p></details>

## 2. Add two Numbers:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.  
You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

<details><summary>sol</summary>
<p>

#### linked list with dummy. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        node = head = ListNode(0)
        while l1 or l2 or carry:
            nextVal = 0
            l1v, l2v = 0, 0
            if l1:
                l1v = l1.val
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2 = l2.next
            if l1v + l2v + carry >= 10:
                node.next = ListNode(l1v + l2v + carry - 10)
                carry = 1
            else:
                node.next = ListNode(l1v + l2v + carry)
                carry = 0
            node = node.next
        return head.next
```
</p></details>

## 3.Longest substring without repeating characters:
Given a string, find the length of the longest substring without repeating characters.  

<details><summary>sol</summary>
<p>

#### use a dictionary to store the last occurrence. a variable start to save the start point of string. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, l, start = 0, 0, 0
        last = {}
        for i, c in enumerate(s):
            if c not in last or last[c] < start:
                l += 1
            else:          
                l = i - last[c]
                start = last[c] + 1
            last[c] = i
            res = max(res, l)
        return res
```
</p></details>

## 4. Median of two Sorted Array
There are two sorted arrays nums1 and nums2 of size m and n respectively.  
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).  
You may assume nums1 and nums2 cannot be both empty.  

<details><summary>sol</summary>
<p>

#### first make sure one’s length greater than the other.
Second, do binary search. l=0, r=m, i = (l+r)/2, j=halfLen-i
compare A[i-1] and B[j]; compare A[i] and B[j-1] to adjust l and r. Else: (found good partition), determine the largest left and smallest right, calculate. time=O(log(min(m, n))), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n:   #make sure len(A) < len(B)
            A, B, m, n = B, A, n, m
        l, r, halfLen = 0, m, (n+m+1)/2
        while l <= r:
            i = (l+r)/2
            j = halfLen - i
            if i > 0 and A[i-1] > B[j]:
                r = i - 1
            elif i < m and A[i] < B[j-1]:
                l = i + 1
            else:   #good i partition
                if i == 0:
                    Lmax = B[j-1]
                elif j == 0:
                    Lmax = A[i-1]
                else:
                    Lmax = max(A[i-1], B[j-1])
                if (m+n)%2 == 1:
                    return Lmax
                if i == m:
                    Rmin = B[j]
                elif j == n:
                    Rmin = A[i]
                else:
                    Rmin = min(A[i], B[j])
                return (Lmax+Rmin)/2.0
```
</p></details>

## 5.Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.  

<details><summary>sol</summary>
<p>

#### Can AC using naive solution : expand from center. for each i or i&i+1, try their best time=O(n^2), space=O(1). / Manacher's Algorithm time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        
        def expand(left: int, right: int):
            while  left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left, right = left-1, right+1
            return left+1, right-1
        
        for i, letter in enumerate(s):
            l, r = expand(i, i)
            if r - l > end - start:
                start, end = l, r
            l, r = expand(i-1, i)
            if r - l > end - start:
                start, end = l, r

        return s[start:end+1]
```
</p></details>

## 6.Zigzag conversion:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P    A    H    N  
A P L S  I  I  G  
Y     I     R  
And then read line by line: "PAHNAPLSIIGYIR"  
Write the code that will take a string and make this conversion given a number of rows:  
string convert(string s, int numRows);  

<details><summary>sol</summary>
<p>

#### use string for each row, and finally join them. much more concise. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        g = [''] * numRows
        if numRows == 1 or numRows > len(s):
            return s
        y, dy = 0, 1
        for c in s:
            g[y] += c
            y += dy
            if y == 0:
                dy = 1
            if y == numRows - 1:
                dy = -1
        return ''.join(g)
```
</p></details>

## 7.Reverse Integer:
Given a 32-bit signed integer, reverse digits of an integer.  
Note:  
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.  

<details><summary>sol</summary>
<p>

#### deal with sign, multiple and range independently. Finally multiply them together. (make use of True == 1, False==0). time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) - (x < 0)
        res = 0
        x = abs(x)
        while x > 0:
            res = res*10 + x%10
            x = x//10
        return sign * res * (res < 2**31)
```
</p></details>

## 8. String to Integer (atoi)
Implement atoi which converts a string to an integer.  
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.  
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.  
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.  
If no valid conversion could be performed, a zero value is returned.  
Note:  
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.  

<details><summary>sol</summary>
<p>

#### stupid question. handle i carefully(preventing index out of range error). time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res, i, sign = 0, 0, 1
        if not str:
            return 0
        while i < len(str)-1 and str[i] == ' ':
            i += 1
        if str[i] in ['+', '-']:
            sign = 1 if str[i] == '+' else -1
            i += 1
        while i < len(str) and str[i].isnumeric():
            res = 10*res + int(str[i])
            i += 1
        return min(res*sign, 2**31-1) if sign == 1 else max(res*sign, -2**31) 
        
```
</p></details>

## 9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.  

<details><summary>sol</summary>
<p>

#### Use an reverse integer to compare. case: num<0, num%10==0. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return x == reverse or x == reverse//10
```
</p></details>

## 10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.  
'.' Matches any single character.  
'*' Matches zero or more of the preceding element.  
The matching should cover the entire input string (not partial).  
Note:  
s could be empty and contains only lowercase letters a-z.  
p could be empty and contains only lowercase letters a-z, and characters like . or *.  

<details><summary>sol1</summary>
<p>

#### recursive. if p empty then s should be empty. compare the first letter in s and p. '*' indicates duplicate or just ignore it. PogChamp complexity, check leetcode.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: # if pattern is empty, str should be empty
            return not s
        firstMatch = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':  #no or lots
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:   #no *, compare first and the rest
            return firstMatch and self.isMatch(s[1:], p[1:])
```
</p></details>

<details><summary>sol2</summary>
<p>

#### DP. time=O(m*n), space=O(m*n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[-1][-1] = True
        for i in range(len(p)-1, -1, -1):
            for j in range(len(s), -1, -1):
                first_match = j < len(s) and p[i] in [s[j], '.']
                if i+1 < len(p) and p[i+1] == '*':
                    dp[i][j] = dp[i+2][j] or (first_match and dp[i][j+1])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
```
</p></details>
