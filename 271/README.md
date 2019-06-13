## 271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.  

<details><summary>sol</summary>
<p>

#### encode: len1/str1len2/str2..., decode: use str.find('/', i) to find the slash and get length information.

</p></details>

<details><summary>code</summary>
<p>

```python
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        for string in strs:
            s += str(len(string)) + '/' + string
        return s

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            # find the slash's position
            j = s.find('/', i+1)
            length = int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i = j+length+1
        return strs

```
</p></details>

## 274. H-Index
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.  
According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."  

<details><summary>sol1</summary>
<p>

#### sort and find. time=O(nlogn) space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        for h in range(len(citations), 0, -1):
            if citations[len(citations)-h] >= h:
                return h
        return 0
```
</p></details>

<details><summary>sol2</summary>
<p>

#### count and find. time=O(n) space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        count = [0] * (n+1)
        for citation in citations:
            count[min(n, citation)] += 1
        cur = 0
        for h in range(n, -1, -1):
            cur += count[h]
            if cur >= h:
                return h
        return 0
```
</p></details>

## 275. H-Index II
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.  
According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."  



<details><summary>sol</summary>
<p>

#### binary search. compare citations[mid] and len-mid. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        l, r = 0, length-1
        while l <= r:
            mid = (l+r) // 2
            if citations[mid] < length - mid:
                l = mid + 1
            elif citations[mid] > length - mid:
                r = mid - 1
            else:
                return citations[mid]
        return length - l

```
</p></details>

## 278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.  
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.  
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.  

<details><summary>sol</summary>
<p>

#### binary search. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            isBad = isBadVersion(mid)
            if isBad:
                r = mid - 1
            else:
                l = mid + 1
        return l
```
</p></details>

## 280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

<details><summary>sol</summary>
<p>

#### Just iterate through nums and swap if violating the requirement. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if i % 2 == 0:
                if i+1 < len(nums) and num > nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            else:
                if i+1 < len(nums) and num < nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
```
</p></details>

## 276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.  
You have to paint all the posts such that no more than two adjacent fence posts have the same color.  
Return the total number of ways you can paint the fence.  
Note:  
n and k are non-negative integers.

<details><summary>sol</summary>
<p>

#### DP with two variables : sameColor and diffColor. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # backtracking TLE. Should use DP.
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        elif n == 2:
            return k * k
        sameColor, diffColor = k, k * (k-1)
        for i in range(3, n+1):
            tmp = diffColor
            diffColor = (sameColor+diffColor) * (k-1)
            sameColor = tmp
        return sameColor + diffColor

```
</p></details>

## 277. Find the Celebrity
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.  
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).  
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.  

<details><summary>sol</summary>
<p>

#### two pass - find the candidate -> check. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
```
</p></details>

## 279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.  

<details><summary>sol</summary>
<p>

#### DP. Since our task is to divide the numbers by perfect square numbers, we can seperate a num i into j*j and (i-j*j) and apply DP. Normal DP will TLE, need to use static(class) variables. time=O(n * sqrtn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # backtracking TLE. Simple DP TLE. have to use static DP
        dp = self._dp
        while len(dp) < n+1:
            best = float('inf')
            i, j = len(dp), 1
            while j*j <= i:
                best = min(best, dp[i - j*j] + 1)
                j += 1
            dp.append(best)
        return dp[n]
            
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
