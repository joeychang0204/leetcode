## 251. Flatten 2D Vector
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.  

<details><summary>sol</summary>
<p>

#### check the total length when initializing. Use the generator(yield) to iterate. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.length = 0
        for vector in v:
            self.length += len(vector)
        def it():
            for vector in v:
                for num in vector:
                    self.length -= 1
                    yield num
        self.iterator = it()

    def next(self) -> int:
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.length > 0
```
</p></details>

## 252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.  

<details><summary>sol</summary>
<p>

#### sort using start time. time=O(nlogn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))

```
</p></details>

## 253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.  

<details><summary>sol1</summary>
<p>

#### use min heap to keep track of the min end time. If the start time >= min end time, then we can use that room. time=O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # min heap with end time
        h = []
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(h, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, intervals[i][1])
        return len(h)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### sort start time and end time individually, use 2 pointers and compare start[sptr] and end[eptr]. If start >= end, then we can use that room. time=O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # handling start time and end time individually
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        rooms = 0
        sptr, eptr = 0, 0
        while sptr < len(intervals):
            if start[sptr] < end[eptr]:
                rooms += 1
            else:
                eptr += 1
            sptr += 1
        return rooms
```
</p></details>

## 254. Factor Combinations
Numbers can be regarded as product of its factors. For example,  
8 = 2 x 2 x 2; = 2 x 4.  
Write a function that takes an integer n and return all possible combinations of its factors.  

<details><summary>sol</summary>
<p>

#### recursion with start. remember to add the number itself. time=space=???

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def getFactors(self, n: int):
        def helper(n, start):
            res = []
            i = start
            while i * i <= n:
                if n % i == 0:
                    # remember to add i and n//i themselves
                    l = helper(i, i)+[[i]]
                    r = helper(n//i, i)+[[n//i]]
                    for ll in l:
                        for rr in r:
                            res.append(ll+rr)
                i += 1
            return res
        return helper(n, 2)
```
</p></details>

## 255. Verify Preorder Sequence in Binary Search Tree
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.  
You may assume each number in the sequence is unique.  

<details><summary>sol</summary>
<p>

#### stack. for each element, pop all elements in stack which is smaller than the element. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = -float('inf')
        stack = []
        for p in preorder:
            if p < lower:
                return False
            while stack and stack[-1] < p:
                lower = stack.pop()
            stack.append(p)
        return True
```
</p></details>

<details><summary>sol2</summary>
<p>

#### similar to sol1, maintain the stack in the original array. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
def verifyPreorder(self, preorder) -> bool:
        lower = -float('inf')
        stack_ptr = -1
        for i, p in enumerate(preorder):
            if p < lower:
                return False
            while stack_ptr >= 0 and p > preorder[stack_ptr]:
                lower = preorder[stack_ptr]
                stack_ptr -= 1
            stack_ptr += 1
            preorder[stack_ptr] = p
        return True
```
</p></details>

## 256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.  
The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.  
Note: All costs are positive integers.  

<details><summary>sol</summary>
<p>

#### simple DP. pick the min between prev[(j+1)%3] and prev[(j+2)%3]. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        for i, cost in enumerate(costs):
            if i > 0:
                prev = costs[i-1]
                for j in range(3):
                    costs[i][j] += min(prev[(j+1)%3], prev[(j+2)%3])
        return min(costs[-1])

```
</p></details>

## 257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.  
Note: A leaf is a node with no children.  

<details><summary>sol1</summary>
<p>

#### recursive, time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # recursive
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        res = []
        if root.left:
            left = self.binaryTreePaths(root.left)
            for l in left:
                res.append(str(root.val) + '->' + l)
        if root.right:
            right = self.binaryTreePaths(root.right)
            for r in right:
                res.append(str(root.val) + '->' + r)
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iterative, time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        # iterative
        if not root:
            return []
        stack = [(root, str(root.val))]
        res = []
        while stack:
            cur = stack.pop(0)
            node, path = cur[0], cur[1]
            if node.left:
                stack.append((node.left, path + '->'+ str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->'+str(node.right.val)))
            if not node.left and not node.right:
                res.append(path)
        return res
```
</p></details>

## 258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.  

<details><summary>sol</summary>
<p>

#### observing question, the pattern repeat every 9 numbers so mod 9. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def addDigits(self, num: int) -> int:
        # 38 - 2, 37 - 1 , 36 - 9 
        if num ==0:
            return 0
        return (num-1) % 9 + 1
```
</p></details>

## 259. 3Sum Smaller
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.  

<details><summary>sol</summary>
<p>

#### two pointers. move the right pointer if sum>=target; else update the result and move the left. Remember to sort first!! time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # sort first!!
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] >= target:
                    k -= 1
                else:
                    res += k-j
                    j += 1
        return res

```
</p></details>

## 260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.  

<details><summary>sol</summary>
<p>

#### 3 steps - 1: XOR all the elements, will get axorb. 2: find a bit in axorb that is 1, which means a and b are different at that bit. 3: XOR the elements with 1/0 at that bit, a and b will be the final outcome. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        axorb = 0
        for num in nums:
            axorb ^= num
        mask = 1
        while mask & axorb == 0:
            mask = mask << 1
        a, b = 0, 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]

```
</p></details>
