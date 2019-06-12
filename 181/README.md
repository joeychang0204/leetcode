## 181. 
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

## 182. 
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

## 183. 
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

## 184. 
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

## 185. 
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

## 186. Reverse Words in a String II
Given an input string , reverse the string word by word. 

<details><summary>sol</summary>
<p>

#### first reverse the list, then reverse each word, time=O(n), space=O(1). 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        for i, ch in enumerate(s):
            if ch == " " or i == len(s)-1:
                l = start
                r = i-1 if ch==" " else i
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l, r = l+1, r-1
                start = i + 1
```
</p></details>

## 187. Repeated DNA Sequence
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.  
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

<details><summary>sol</summary>
<p>

#### brute force using two set seen and repeated. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        for i in range(len(s)-9):
            cur = s[i:i+10]
            repeated.add(cur) if cur in seen else seen.add(cur)
        return list(repeated)

```
</p></details>

## 188. 
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

## 189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

<details><summary>sol1</summary>
<p>

#### naive using list slices, time = O(n), space = O(n) (list slicing take O(k) time where k is the len of slice, O(n) space). 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        #sol1:
        #assigning using nums[:] so can write to the original nums
        nums[:] = nums[-k:] + nums[:-k]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### reverse three times : the entire list, the first half, the second half. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l

        #sol2:
        if not nums:
            return
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        reverse(nums, 0, l-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, l-1)
```
</p></details>

## 190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

<details><summary>sol</summary>
<p>

#### res start from 0, using bit manipulation. time = O(1), space = O(1). (bitwise operators' priority are less than +, -, so brackets are necessary)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            #() is necessary!!
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res

```
</p></details>
