## 41. 
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

## 42. 
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

## 43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.  
Note:  
The length of both num1 and num2 is < 110.  
Both num1 and num2 contain only digits 0-9.  
Both num1 and num2 do not contain any leading zero, except the number 0 itself.  
You must not use any built-in BigInteger library or convert the inputs to integer directly.  

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

## 44. 
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

## 45. 
description

<details><summary>sol</summary>
<p>

#### 

</p></details>

<details><summary>code</summary>
<p>

```python
```
</p></details>

## 46. Permutations
Given a collection of distinct integers, return all possible permutations.

<details><summary>sol1</summary>
<p>

#### basic backtracking. time=O(n!), space=O(n!) for solutions.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def permute(self, nums):
        res = []
        def backtrack(cur):
            if(len(cur) == len(nums)):
                res.append(cur)
                return
            for num in nums:
                if num not in cur:
                    backtrack(cur+[num])
        backtrack([])
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iteratively. time=space=O(n*(n!)) ??

</p></details>

<details><summary>code</summary>
<p>

```python
    def permute2(self, nums):
        #iterative sol
        res = [[]]
        for num in nums:
            new_res = []
            for r in res:
                #be careful of this range
                for i in range(len(r)+1):
                    new_res.append(r[:i]+[num]+r[i:])
            res = new_res
        return res
```
</p></details>



## 47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.  

<details><summary>sol</summary>
<p>

#### similar to 46, but have to handle duplicates

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 48.Rotate Image
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).  
Note:  
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.  

<details><summary>sol</summary>
<p>

#### first transpose, next reverse. time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
```
</p></details>

## 49. group anagrams
Given an array of strings, group anagrams together.  
Example:  
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],  
Output:  
[  
["ate","eat","tea"],  
["nat","tan"],  
["bat"]  
]  
Note:  
All inputs will be in lowercase.  
The order of your output does not matter.  

<details><summary>sol</summary>
<p>

#### use dictionary to solve this problem. key for dic : sorted word/character count of word/26 primes timing integer. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    #use the sorted words as key
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            cur = str(sorted((word)))
            prev = dic.get(cur, [])
            prev.append(word)
            dic[cur] = prev
        res = []
        for k, v in dic.items():
            res.append(v)
        return res

    #use the word's character count as key
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            dic[str(count)] = dic.get(str(count), []) + [word]
        res = []
        for k,v in dic.items():
            res.append(v)
        return res

```
</p></details>

## 50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (x^n).

<details><summary>sol1</summary>
<p>

#### iterative. if the right-most bit is 1, multiply the result by x, x^2, x^4..., and then right shift n.time=O(logn), space=O(1) 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    # iterative
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        res = 1.0
        while n > 0:
            if n & 1:
                res *= x
            n = n >> 1
            x *= x
        return res

```
</p></details>

<details><summary>sol2</summary>
<p>

#### recursive. x^n = (x^2)^(n/2) or x*(x^2)^(n//2). time=O(logn), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1/x
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x*x, int(n/2))
```
</p></details>
