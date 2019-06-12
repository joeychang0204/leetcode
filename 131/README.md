## 131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.  
Return all possible palindrome partitioning of s.

<details><summary>sol</summary>
<p>

#### use dfs, split word from 1 to end, dfs further if first part is palindrome. append result when word is empty. time=O(n*(2^n)), space??

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        if not s:
            return []
        def dfs(word, part):
            if not word:
                self.res.append(part)
                return
            for i in range(1, len(word)+1):
                if word[:i] == word[:i][::-1]:
                    dfs(word[i:], part+[word[:i]])
        dfs(s, [])
        return self.res

```
</p></details>

## 132. 
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

## 133. Clone Graph
Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.

<details><summary>sol</summary>
<p>

#### use a global dictionary to store nodes. case : node pointing to itself. time=O(nm) where m is the number of edges, space=O(nm)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.d = {}
    def cloneGraph(self, node):
        if not node:
            return
        if self.d.get(node.label):
            return self.d.get(node.label)
        
        cur = UndirectedGraphNode(node.label)
        self.d[node.label] = cur
            
        for neighbor in node.neighbors:
            cur.neighbors.append(self.cloneGraph(neighbor))
        return cur

```
</p></details>

## 134. Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].  
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.  
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.  
  
Note:  
If there exists a solution, it is guaranteed to be unique.  
Both input arrays are non-empty and have the same length.  
Each element in the input arrays is a non-negative integer.

<details><summary>sol</summary>
<p>

#### observation : if A cannot reach B, any station between A and B cannot reach B (proof by contradiction) -> set the next index as start and check the subsum from it. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, cur = 0, 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start
```
</p></details>

## 135. 
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

## 136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.  
  
Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

<details><summary>sol</summary>
<p>

#### XOR. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

```
</p></details>

## 137. Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.  
  
Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

<details><summary>sol</summary>
<p>

#### [somehow magically](https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1, x2 = 0, 0
        for num in nums:
            x2 ^= (x1 & num)
            x1 ^= num
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x1
        

```
</p></details>

## 138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.  

Return a deep copy of the list.

<details><summary>sol1</summary>
<p>

#### global dictionary, be careful with the position assigning the value of dictionary. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def __init__(self):
        self.d = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        if self.d.get(head.label):
            return self.d.get(head.label)
        cur = RandomListNode(head.label)
        self.d[head.label] = cur
        cur.next = self.copyRandomList(head.next)
        cur.random = self.copyRandomList(head.random)
        #don't assign self.d here, will cause maximum recursion depth exceeded for nodes pointing to itself
        
        return cur
```
</p></details>

<details><summary>sol2</summary>
<p>

#### 1.append copy nodes right after each original nodes. 2. manipulate copy node’s random pointer 3. restore original pointers, build the new copied list. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def copyRandomList2(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        #first round : create copies right after each original node
        node = head
        while node:
            next = node.next
            node.next = RandomListNode(node.label)
            node.next.next = next
            node = next
        #second round : manipulate random pointers for copies
        node = head
        while node:
            if node.random:
                #node.random may not exist, else its next one should be the copied random node
                node.next.random = node.random.next
            node = node.next.next
        #third round : restore original list, get res
        dummy = copy = RandomListNode(0)
        node = head
        while node:
            copy.next = node.next
            copy = copy.next
            node.next = node.next.next
            node = node.next
        return dummy.next
```
</p></details>

## 139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.  
  
Note:  
The same word in the dictionary may be reused multiple times in the segmentation.  
You may assume the dictionary does not contain duplicate words.

<details><summary>sol1</summary>
<p>

#### naive recursion will TLE, can do the recursion with memo, record each string after checking the first time. time=??, space=??

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def __init__(self):
        self.memo = {}
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if self.memo.get(s) is not None:
            return self.memo.get(s)
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False
```
</p></details>

<details><summary>sol2</summary>
<p>

#### dp, substring can break(dp = True) and the rest in dict -> dp = true. time=O(n^2), space=O(L)

</p></details>

<details><summary>code</summary>
<p>

```python
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
```
</p></details>

## 140. 
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
