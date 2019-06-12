## 161. One Edit Distance
Given two strings s and t, determine if they are both one edit distance apart.  
There are 3 possiblities to satisify one edit distance apart:  
Insert a character into s to get t  
Delete a character from s to get t  
Replace a character of s to get t

<details><summary>sol</summary>
<p>

#### iterate from the first char of strings, when different, compare the remaining parts. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = min(len(s), len(t))
        for i in range(l):
            if s[i] != t[i]:
                if len(s) > len(t):
                    return s[i+1:] == t[i:]
                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len(s) - len(t)) == 1
```
</p></details>

## 162. Find Peak Element
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞

<details><summary>sol</summary>
<p>

#### binary search. go to the bigger direction since the peak is there. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
```
</p></details>

## 163. Missing Ranges
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

<details><summary>sol</summary>
<p>

#### comparing prev and num. **initialization
(prev to lower-1, append upper+1 to nums). time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower - 1
        nums.append(upper+1)
        for num in nums:
            if num-prev == 2:
                res.append(str(num-1))
            elif num-prev > 2:
                res.append(str(prev+1) + '->' + str(num-1))
            prev = num
        return res
```
</p></details>

## 164. 
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

## 165. Compare Version Numbers
Compare two version numbers version1 and version2.  
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.  
You may assume that the version strings are non-empty and contain only digits and the . character.  
The . character does not represent a decimal point and is used to separate number sequences.  
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.  
You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

<details><summary>sol</summary>
<p>

#### split, adding zeros, compare. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        while len(v1) != len(v2):
            if len(v1) < len(v2):
                v1.append('0')
            else:
                v2.append('0')
        for i, _ in enumerate(v1):
            n1, n2 = int(v1[i]), int(v2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0

```
</p></details>

## 166. Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.  
If the fractional part is repeating, enclose the repeating part in parentheses.  

<details><summary>sol</summary>
<p>

#### first divide once, determine if there’s ‘.’. In the while loop, do the similar thing. Use a dictionary to record where the numerator appeared. case : negative result, long number 2147483648 is ok in Python. time=space=O (denominator)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        res = ""
        if numerator * denominator < 0:
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        numerator = (numerator % denominator) * 10
        if numerator > 0:
            res += '.'
        i = len(res)
        d = {}
        while numerator > 0:
            d[numerator] = i
            res += str(numerator // denominator)
            numerator = (numerator % denominator) * 10
            if numerator in d.keys():
                res = res[:d[numerator]] + '(' + res[d[numerator]:] + ')'
                break
            i += 1
        return res
```
</p></details>

## 167. Two Sum II - Input Array is Sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.  
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.  

Note:  
Your returned answers (both index1 and index2) are not zero-based.  
You may assume that each input would have exactly one solution and you may not use the same element twice.

<details><summary>sol</summary>
<p>

#### two pointers. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]

```
</p></details>

## 168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.  
For example:  
1 -> A  
2 -> B  
3 -> C  
...  
26 -> Z  
27 -> AA  
28 -> AB 

<details><summary>sol</summary>
<p>

#### like changing the base of integer, note that if n % 26 == 0, should add ‘Z’ and minus n by 1. case : 52 -> AZ, not B something. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #ch = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        ch = ['Z'] + [chr(ord('A') + i) for i in range(26)]
        res = ""
        while n > 0:
            res += ch[n%26]
            if n % 26 == 0:
                n -= 1
            n = n // 26
        return res[::-1]
```
</p></details>

## 169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.  
You may assume that the array is non-empty and the majority element always exist in the array.

<details><summary>sol</summary>
<p>

#### Boyer-Moore Voting Algorithm : If meet the same element, counter += 1, else -=1. Change the candidate if counter == 0.

</p></details>

<details><summary>code</summary>
<p>

```python
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter , candidate = 0, None
        for num in nums:
            if counter == 0:
                candidate = num
            if candidate == num:
                counter += 1
            else:
                counter -= 1
        return candidate
```
</p></details>

## 170. Two Sum III - Data Structure Design
Design and implement a TwoSum class. It should support the following operations: add and find.  
add - Add the number to an internal data structure.  
find - Find if there exists any pair of numbers which sum is equal to the value.

<details><summary>sol</summary>
<p>

#### use dictionary. iterate through the keys and check num-key in dictionary. space=O(n).add time=O(1), find time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.d[number] = self.d.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.d:
            if  value - num in self.d and num != value-num:
                return True
            elif num == value-num and self.d[num] > 1:
                return True
        return False
```
</p></details>
