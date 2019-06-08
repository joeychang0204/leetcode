## 291.
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

## 292. Nim Game
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.  
Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.  

<details><summary>sol</summary>
<p>

#### Check n%4 != 0. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 0:
            return False
        return n % 4 != 0
        
```
</p></details>

## 293. Flip Game
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.  
Write a function to compute all possible states of the string after one valid move.  

<details><summary>sol</summary>
<p>

#### Note that for strings like 'yoyo', s[100:] is valid and will return empty string.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i, letter in enumerate(s):
            if letter == '+' and i > 0 and s[i-1] == '+':
                res.append(s[:i-1] + '--' + s[i+1:])
        return res

```
</p></details>

## 294. Flip Game II
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.  
Write a function to determine if the starting player can guarantee a win.  



<details><summary>sol</summary>
<p>

#### backtracking. when fing '++', make it '--' and gogo. T(N) = (N-2) * T(N-2) = (N-2) * (N-4) * T(N-4) ... = (N-2) * (N-4) * (N-6) * ... ~ O(N!!). space = O(N)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def canWin(self, s: str) -> bool:
        # backtracking / hard DP
        if not s:
            return False
        for i, ch in enumerate(s):
            if i < len(s) - 1 and ch == s[i+1] == '+':
                if not self.canWin(s[:i] + '--' + s[i+2:]):
                    return True
        return False
```
</p></details>

## 295. 
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

## 296. 
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

## 297. 
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

## 298. Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.  
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).  

<details><summary>sol</summary>
<p>

#### top-down dfs.(can also try bottom-up) time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, l):
            if not node:
                return
            self.res = max(self.res, l)
            for child in [node.left, node.right]:
                if child and child.val == node.val + 1:
                    dfs(child, l+1)
                else:
                    dfs(child, 1)
        dfs(root, 1)
        return self.res
```
</p></details>

## 299. Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.  
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.  
Please note that both secret number and friend's guess may contain duplicate digits.  

<details><summary>sol</summary>
<p>

#### One pass using dictionary as counter. for secret / guess, increase / decrease the counter by 1. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = collections.defaultdict(int)
        A, B = 0, 0
        for i, s in enumerate(secret):
            g = guess[i]
            if g == s:
                A += 1
            else:
                if count[g] < 0:
                    B += 1
                if count[s] > 0:
                    B += 1
                count[g] += 1
                count[s] -= 1
        return str(A) + 'A' + str(B) + 'B'
```
</p></details>

## 300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.  

<details><summary>sol1</summary>
<p>

#### traverse from last, use dict for each number's best. time=O(n^2), space=O(n)

</p></details>

<details><summary>code1</summary>
<p>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = collections.defaultdict(int)
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            best = 1
            for k, v in longest.items():
                if k > num:
                    best = max(best, 1+v)
            longest[num] = best
        return max(list(longest.values()))
```
</p></details>
