## 241. Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.  

<details><summary>sol</summary>
<p>

#### iterate through the input, when meet operators, recursively solve left part and right part. time = [Catalan Number] (http://people.math.sc.edu/howard/Classes/554b/catalan.pdf), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if len(input) <= 3:
            return [eval(input)]
        res = []
        for i, num in enumerate(input):
            if num in '+-*/':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for r1 in res1:
                    for r2 in res2:
                        res.append(eval(str(r1) + num + str(r2)))
        return res

```
</p></details>

## 242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.  
(anagram : rearranging the letters of another)  
Note:  
You may assume the string contains only lowercase alphabets.  
Follow up:  
What if the inputs contain unicode characters? How would you adapt your solution to such case?  

<details><summary>sol1</summary>
<p>

#### compare collections.Counter for list(s) and list(t), time = O(n), space=O(1) for lowercase alphabets(26 possibilities)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(list(s)) == collections.Counter(list(t))
```
</p></details>

<details><summary>sol2</summary>
<p>

#### sort and compare, time=O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
```
</p></details>

## 243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.  

<details><summary>sol</summary>
<p>

#### initialize the positions to -1. if both are not -1, update the result. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # concise one-pass
        pos1, pos2 = -1, -1
        res = len(words)
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1-pos2))
        return res
```
</p></details>

## 244. Shortest Word Distance II
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.  

<details><summary>sol</summary>
<p>

#### preprocess each word's index. Use the index to find distance for each query. space=O(n), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class WordDistance:

    def __init__(self, words: List[str]):
        self.words = words
        self.index = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.index[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = len(self.words)
        i, j = 0, 0
        while i < len(self.index[word1]) and j < len(self.index[word2]):
            index1, index2 = self.index[word1][i], self.index[word2][j]
            res = min(res, abs(index1-index2))
            if index1 < index2:
                i += 1
            else:
                j += 1
        return res

```
</p></details>

## 245. Shortest Word Distance III
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.  
word1 and word2 may be the same and they represent two individual words in the list.  

<details><summary>sol</summary>
<p>

#### similar to Q243 but have to handle same word case. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = -1, -1
        res = len(words)
        for i, word in enumerate(words):
            if word == word1 and word1 == word2:
                if pos1 <= pos2:
                    pos1 = i
                else:
                    pos2 = i
            elif word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1-pos2))
        return res

```
</p></details>

## 246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).  
Write a function to determine if a number is strobogrammatic. The number is represented as a string.  

<details><summary>sol</summary>
<p>

#### check if all num and its corresponding num is in [00, 11, 88, 69, 96]. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        return all(num[i] + num[len(num)-1-i] in ['69', '96', '88', '00', '11']
                  for i in range(len(num)))

```
</p></details>

## 247. Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).  
Find all strobogrammatic numbers that are of length = n. 

<details><summary>sol</summary>
<p>

#### brute force using Q246's technique -> TLE. sol: backtracking from middle, time=O(5^(n/2)), space=O(5^(n/2))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidates = ['00', '11', '88', '69', '96']
        res = []
        def backtrack(cur):
            if len(cur) == n:
                if n > 1 and cur[0] == '0':
                    return
                res.append(cur)
                return
            if len(cur) == 0 and n % 2 == 1:
                backtrack('1')
                backtrack('0')
                backtrack('8')
            else:
                for c in candidates:
                    backtrack(c[0] + cur + c[1])
        backtrack('')
        return res
                    

```
</p></details>

## 248. 
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

## 249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:  
"abc" -> "bcd" -> ... -> "xyz"  
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.  

<details><summary>sol</summary>
<p>

#### sol : use the len + differences between each letter as key, build the dictionary. time=O(nlen), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # WA : az, ba -> have to %26
        grouped = {}
        for s in strings:
            key = str(len(s))
            for i in range(len(s)):
                if i == 0:
                    continue
                key += str((ord(s[i])-ord(s[i-1])) % 26)
            grouped[key] = grouped.get(key, []) + [s]
        # RE: values not returning list in Python3, have to wrap
        return list(grouped.values())
```
</p></details>

## 250. Count Univalue Subtrees
Given a binary tree, count the number of uni-value subtrees.  
A Uni-value subtree means all nodes of the subtree have the same value.  

<details><summary>sol</summary>
<p>

#### easy DFS. time=O(n), space=O(h)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            l_value = node.left.val if node.left else node.val
            r_value = node.right.val if node.right else node.val
            isUni = l and r and l_value == node.val and r_value == node.val
            if isUni:
                self.res += 1
            return isUni
        dfs(root)
        return self.res
```
</p></details>
