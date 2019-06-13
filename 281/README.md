## 281. Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.  

<details><summary>sol</summary>
<p>

#### Use a list of tuples (len, iter). Pop the first and push back if len-1 > 0. time=O(n), space=O(1)?

</p></details>

<details><summary>code</summary>
<p>

```python
class ZigzagIterator(object):
    # use lists too suck, try use iterator!
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [(len(v), iter(v)) for v in v1, v2 if v]

    def next(self):
        """
        :rtype: int
        """
        length, it = self.data.pop(0)
        res = next(it)
        if length-1 > 0:
            self.data.append((length-1, it))
        return res
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)

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

## 283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.  
Note:  
You must do this in-place without making a copy of the array.  
Minimize the total number of operations.  



<details><summary>sol</summary>
<p>

#### Use a nonZero pointer. Swap when meet non zero number. time=O(n), space=O(1), operations=number of non-zeros 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonZero] = nums[nonZero], nums[i]
                nonZero += 1
```
</p></details>

## 284. Peeking Iterator
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().  

<details><summary>sol</summary>
<p>

#### Use a tmp variable for the next, update it when calling next(). time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.tmp = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp
        

    def next(self):
        """
        :rtype: int
        """
        res = self.tmp
        self.tmp = self.it.next() if self.it.hasNext() else None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.tmp is not None
```
</p></details>

## 285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.  
The successor of a node p is the node with the smallest key greater than p.val.  

<details><summary>sol</summary>
<p>

#### PogChamp beautiful recursion. time=O(logn), space=O(logn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root
```
</p></details>

## 286. Walls and Gates
You are given a m x n 2D grid initialized with these three possible values.  
-1 - A wall or an obstacle.  
0 - A gate.  
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.  
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.  



<details><summary>sol1</summary>
<p>

#### DFS from gates + visited, slow and verbose

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # DFS
        visited = [[False] * len(rooms[0]) for i in range(len(rooms))]
        def dfs(i, j, distance):
            if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
                return
            if visited[i][j]:
                return
            if rooms[i][j] <= 0 and distance > 0 :
                return
            rooms[i][j] = min(rooms[i][j], distance)
            visited[i][j] = True
            for di, dj in (1,0), (0,1), (-1,0), (0,-1):
                dfs(i+di, j+dj, distance+1)
            visited[i][j] = False
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### BFS from gates, concise and fast. time=O(mn), space=O(mn)

</p></details>

<details><summary>code</summary>
<p>

```python
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # BFS
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, distance = queue.pop(0)
            for I, J in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                # if I, J valid and it's an empty room
                if I >= 0 and I < len(rooms) and J >=0 and J < len(rooms[0]) and rooms[I][J] == (2**31) - 1:
                    rooms[I][J] = distance + 1
                    queue.append((I, J, distance + 1))
```
</p></details>

## 287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.  

<details><summary>sol1</summary>
<p>

#### bit manipulation, check the bit while iterating. make use of python integer's arbitrary precision. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = 0
        for num in nums:
            mask = 1 << (num-1)
            if check & mask != 0:
                return num
            check |= mask
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Floyd's cycle detection. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cycle
        if not nums:
            return False
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```
</p></details>

## 288. Unique Word Abbreviation
An abbreviation of a word follows the form <first letter><number><last letter>.  
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.  

<details><summary>sol</summary>
<p>

#### Use dict to solve. time=O(1), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = collections.defaultdict(list)
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
            # WA : for repeated words, only add once
            if word not in self.d[abb]:
                self.d[abb].append(word)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abb = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        # WA: self.d[abb] is a list, have to give it an index
        return len(self.d[abb]) == 0 or (len(self.d[abb]) == 1 and self.d[abb][0] == word)
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

```
</p></details>

## 289. Game of Life
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):  
1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.  
2. Any live cell with two or three live neighbors lives on to the next generation.  
3. Any live cell with more than three live neighbors dies, as if by over-population..  
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.  
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.  
  
Follow up:  
1.Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.  
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?  

<details><summary>sol</summary>
<p>

#### first pass update the cells while preserving original information. second pass correct the output. time=O(mn), space=O(1).  
#### follow up: Only save the location of live cells, simulate according to the live cells. To save the space, can only keep the last 3 rows.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def getNext(i, j):
            neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            live = 0
            for I, J in neighbors:
                if I>=0 and I<len(board) and J>=0 and J<len(board[0]):
                    if board[I][J] >= 1:
                        live += 1
            if board[i][j] == 1:
                return 11 if (live==2 or live==3) else 10
            else:
                return -9 if live==3 else 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = getNext(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] %= 10

```
</p></details>

## 290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.  
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.  

<details><summary>sol1</summary>
<p>

#### dictionary. have to check d.values(), not like this. time=O(n), space=O(n).

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        words = str.split()
        if len(words) != len(pattern):
            return False
        for i, word in enumerate(words):
            if word in d and d[word] != pattern[i]:
                return False
            elif word not in d and pattern[i] in list(d.values()):
                return False
            d[word] = pattern[i]
        return True
```
</p></details>

<details><summary>sol2</summary>
<p>

#### using map to compare the first appearance of each word in pattern and str.  

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        # have to add 'list' in front of map for python3
        return list(map(words.index, words)) == list(map(pattern.find, pattern))

```
</p></details>
