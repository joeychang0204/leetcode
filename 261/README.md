## 261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.  
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges. 

<details><summary>sol</summary>
<p>

#### tree - acyclic + connected. union find. merge one's root under the other's root. check the number of edges at the end(for connected). time=O(n^2), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [-1] * n
        def find(p):
            return p if parent[p] == -1 else find(parent[p])
        for edge in edges:
            p0, p1 = find(edge[0]), find(edge[1])
            # check cycle
            if p0 == p1:
                return False
            parent[p1] = p0
        return len(edges) == n-1
```
</p></details>

## 263. Ugly Number
Write a program to check whether a given number is an ugly number.  
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.  
Note:  
1 is typically treated as an ugly number.  
Input is within the 32-bit signed integer range: [−231,  231 − 1].  

<details><summary>sol</summary>
<p>

#### easy while loop time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for prime in [2, 3, 5]:
            while num % prime == 0:
                num /= prime
        return num == 1
```

</p></details>

## 264. Ugly Number II
Write a program to find the n-th ugly number.  
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.  

<details><summary>sol</summary>
<p>

#### keep calling isUgly will TLE. Use three pointers for 2, 3, 5 and append the min product. Have to update both the pointers for ugly numbers like 6. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = [1]
        p2, p3, p5 = 0, 0, 0
        while len(uglyNums) < n:
            uglyNums.append(min(uglyNums[p2]*2, uglyNums[p3]*3, uglyNums[p5]*5))
            if uglyNums[-1] == uglyNums[p2]*2:
                p2 += 1
            if uglyNums[-1] == uglyNums[p3]*3:
                p3 += 1
            if uglyNums[-1] == uglyNums[p5]*5:
                p5 += 1
        return uglyNums[-1]

        
```

</p></details>

## 266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.  

<details><summary>sol</summary>
<p>

#### use a list(size=128) to count the occurrence of each ascii word. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = [0] * 128
        for letter in s:
            counter[ord(letter)] = 1 - counter[ord(letter)]
        return sum(counter) <= 1
```

</p></details>

## 267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.  

<details><summary>sol</summary>
<p>

#### counter + backtracking. time=O((n/2+1)!), space=O(n) 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        permutation = []
        counter = collections.Counter(s)
        mid = [k for k,v in counter.items() if v%2 == 1]
        if len(mid) > 1:
            return []
        def permute(cur):
            if len(cur) == len(s):
                permutation.append(cur)
                return
            for k,v in counter.items():
                if v >= 2:
                    counter[k] -= 2
                    permute(k + cur + k)
                    counter[k] += 2
        
        mid = mid[0] if len(mid) == 1 else ''
        permute(mid)
        return permutation
```

</p></details>

## 268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.  

<details><summary>sol1</summary>
<p>

#### XOR. time=O(n), space=O(1) 

</p></details>

<details><summary>code1</summary>
<p>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= (i ^ num)
        return xor
```

</p></details>

<details><summary>sol2</summary>
<p>

#### Gauss' Formula to get the sum from 1 to n. time=O(n), space=O(1) 

</p></details>

<details><summary>code2</summary>
<p>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = int((n+1)*n/2)
        return res-sum(nums)
```

</p></details>

## 270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.  
Note:  
Given target value is a floating point.  
You are guaranteed to have only one unique value in the BST that is closest to the target.  


<details><summary>sol1</summary>
<p>

#### recursion. time=O(h), space=O(h) 

</p></details>

<details><summary>code1</summary>
<p>

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return float('inf')
        res = float('inf')
        if target < root.val:
            res = self.closestValue(root.left, target)
        elif target > root.val:
            res = self.closestValue(root.right, target)
        else:
            res = root.val
        return res if abs(res-target) <= abs(root.val-target) else root.val
```

</p></details>

<details><summary>sol2</summary>
<p>

#### iterative. time=O(h), space=O(1)

</p></details>

<details><summary>code2</summary>
<p>

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float('inf')
        while root:
            if abs(root.val-target) < abs(res-target):
                res = root.val
            root = root.left if target <= root.val else root.right
        return res
```

</p></details>


