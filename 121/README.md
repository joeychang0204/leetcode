## 121. Best Time to Buy and Sell stock
Say you have an array for which the ith element is the price of a given stock on day i.  
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.  
  
Note that you cannot sell a stock before you buy one.

<details><summary>sol</summary>
<p>

#### straightforward recording the cheapest and calculate each price's profit. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheapest = float('inf')
        res = 0
        for price in prices:
            res = max(res, price - cheapest)
            cheapest = min(cheapest, price)
        return res

```
</p></details>

## 122. Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.  
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).  
  
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

<details><summary>sol</summary>
<p>

#### find the consecutive peaks and valleys. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(prices):
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            lowest = prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i+1]:
                i += 1
            res += prices[i] - lowest
            i += 1
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### add the adjacent difference if prices[i+1] > prices[i]. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i, _ in enumerate(prices):
            if i > 0 and prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
```
</p></details>

## 123. 
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

## 124. 
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

## 125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

Note: For the purpose of this problem, we define empty string as valid palindrome.

<details><summary>sol</summary>
<p>

#### Two pointers head and tail, skip the invalid characters. use str.isalpha() to check is character, use str.isnumeric() to check is number, use s = s.lower() to make the string lower case. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        head, tail = 0, len(s)-1
        while head <= tail:
            while head < len(s)-1 and not s[head].isalpha() and not s[head].isnumeric():
                head += 1
            while tail > 0 and not s[tail].isalpha() and not s[tail].isnumeric():
                tail -= 1
            
            if head <= tail and s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
```
</p></details>

## 126. 
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

## 127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:  
Only one letter can be changed at a time.  
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.  
Note:  
Return 0 if there is no such transformation sequence.  
All words have the same length.  
All words contain only lowercase alphabetic characters.  
You may assume no duplicates in the word list.  
You may assume beginWord and endWord are non-empty and are not the same.

<details><summary>sol</summary>
<p>

#### naive bfs will TLE, can try two-end BFS. my sol : preprocessing words - abc to ab_, a_c, _bc in a dict, make it easier to find neighbors. time=O(nL) where L is the length of word, space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def toDict(words):
            d = {}
            for word in words:
                for i, _ in enumerate(word):
                    cur = word[:i] + "_" + word[i+1:]
                    d[cur] = d.get(cur, []) + [word]
            return d
        d = toDict(wordList)
        q = [beginWord]
        used = set()
        res = 1
        while q:
            newq = []
            while q:  
                cur = q.pop(0)
                if cur == endWord:
                    return res
                if cur not in used:
                    used.add(cur)
                    for i, _ in enumerate(cur):
                        c = cur[:i] + "_" + cur[i+1:]
                        for word in d.get(c, []):
                            if word not in used:
                                newq.append(word)
            res += 1
            q = newq
        return 0
```
</p></details>

## 128.
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

## 129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.  
An example is the root-to-leaf path 1->2->3 which represents the number 123.  
Find the total sum of all root-to-leaf numbers.  

Note: A leaf is a node with no children.

<details><summary>sol</summary>
<p>

#### dfs recording sum, sum*10 when going to child. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, val):
            if not node:
                return
            val += node.val
            if not node.left and not node.right:
                self.res += val
            dfs(node.left, val*10)
            dfs(node.right, val*10)
        dfs(root, 0)
        return self.res
```
</p></details>

## 130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.  
A region is captured by flipping all 'O's into 'X's in that surrounded region.

<details><summary>sol</summary>
<p>

#### directly modify good “O”s to “G”, check is G at the end. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
        def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board[0]), len(board)
        def dfs(i, j):
            if board[i][j] == "O":
                board[i][j] = "G"
                for k in range(4):
                    di = [1, 0, -1, 0]
                    dj = [0, 1, 0, -1]
                    if 0<=i+di[k]<=n-1 and 0<=j+dj[k]<=m-1:
                        dfs(i+di[k], j+dj[k])
            else:
                return
            
        for j in [0, n-1]:
            for i in range(m):
                dfs(j, i)
        for j in [0, m-1]:
            for i in range(n):
                dfs(i, j)
        for i in range(n):
            for j in range(m):
                board[i][j] = "O" if board[i][j] == "G" else "X"
```
</p></details>
