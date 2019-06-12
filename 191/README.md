## 191. Number of One Bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

<details><summary>sol</summary>
<p>

#### checking the last bit(AND with 1), and then shift. time = O(1) since at most 32 times, space = O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n & 1
            n = n >> 1
        return res
```
</p></details>

## 192. 
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

## 193. 
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

## 194. 
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

## 195. 
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

## 196. 
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

## 197. 
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

## 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.  

<details><summary>sol</summary>
<p>

#### DP. use two integer prevmax and curmax to represent the available maximum

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevmax, curmax = 0, 0
        for num in nums:
            tmp = curmax
            curmax = max(curmax, prevmax + num)
            prevmax = tmp
        return curmax
```
</p></details>

## 199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.  

<details><summary>sol</summary>
<p>

#### DFS/BFS with level. right first. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rightSideView(self, root):
        #BFS
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        queue = [(root, 1)]
        while queue:
            cur = queue.pop(0)
            node, level = cur[0], cur[1]
            if level > len(res):
                res.append(node.val)
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
        return res
    def rightSideView(self, root):
        #DFS
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        def dfs(node, level):
            if not node:
                return
            if level > len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 1)
        return res
```
</p></details>

## 200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.  

<details><summary>sol</summary>
<p>

#### dfs/ bfs, modifying visited '1's. time=O(mn), space=O(mn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #DFS
        if not grid:
            return 0
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        def dfs(i, j):
            #invalid i/j
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1:
                return
            if grid[i][j] == '1':
                grid[i][j] = '*'
                for k in range(4):
                    dfs(i+di[k], j+dj[k])
            else:
                return
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #BFS
        if not grid:
            return 0
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        cur = queue.pop(0)
                        #don't use variables i, j......
                        curi, curj = cur[0], cur[1]
                        if curi < 0 or curj < 0 or curi > len(grid)-1 or curj > len(grid[0])-1:
                            continue
                        if grid[curi][curj] == '1':
                            grid[curi][curj] = '0'
                            for k in range(4):
                                queue.append((curi+di[k], curj+dj[k]))
        return res
```
</p></details>
