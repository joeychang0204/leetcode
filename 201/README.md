## 201. Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

<details><summary>sol</summary>
<p>

#### brute force time = O(n), good sol time = O(1). sol : while m > n, right shift one bit. from xxx0.....  to xxx1..... , must include two numbers differs in the last bit, leading to one more zero. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #101, 110, 111 -> 100
        #O(n) brute force TLE
        zeroes = 0
        while m != n:
            if m == 0:
                return 0
            m >>= 1
            n >>= 1
            zeroes += 1
        return m << zeroes
```
</p></details>

## 202. Happy Number
Write an algorithm to determine if a number is "happy".  

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

<details><summary>sol</summary>
<p>

#### fast and slow. time=O(n), space=O(1). 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def nextHappy(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num =  num // 10
            return res
        fast = slow = n
        while True:
            fast = nextHappy(fast)
            fast = nextHappy(fast)
            slow = nextHappy(slow)
            if slow == fast:
                break
        return slow == 1

```
</p></details>

## 203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.  

<details><summary>sol1</summary>
<p>

#### intuitive dummy head, O(1) space O(n) time, good enough

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        while head:
            if head.val != val:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return dummy.next
```
</p></details>

<details><summary>sol2</summary>
<p>

#### beautiful recursive. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
```
</p></details>

## 204. Count Primes
Count the number of prime numbers less than a non-negative number, n.  

<details><summary>sol1</summary>
<p>

#### O(1) space, brute force calling isPrime will TLE. sol : eliminating multiplies of primes, fastest. space=O(n), time=???

</p></details>

<details><summary>code</summary>
<p>

```python
    def countPrimes(self, n: int) -> int:
        # eliminate prime's mutiples
        if n <= 2:
            return 0
        isPrime = [1] * n
        isPrime[0], isPrime[1] = 0, 0
        i = 2
        while i * i < n:
            if isPrime[i] == 1:
                j = i * 2
                while j < n:
                    isPrime[j] = 0
                    j += i
            i += 1
        return sum(isPrime)
```
</p></details>

## 205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.  
Two strings are isomorphic if the characters in s can be replaced to get t.  
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.  

<details><summary>sol1</summary>
<p>

#### dictionary, note that two keys can't have same value. time=O(max(lens,lent)), space=O(max(lens, lent))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] != t[i]:
                return False
            if ch not in d and t[i] in d.values():
                return False
            d[ch] = t[i]
        return True
```
</p></details>

<details><summary>sol2</summary>
<p>

#### use zip to compress s and t, one line. time=O(max(lens,lent)), space=O(max(lens, lent))

</p></details>

<details><summary>code</summary>
<p>

```python
    def isIsomorphic2(self, s, t):
        print(set(zip(s,t)))
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
```
</p></details>

## 206. Reverse Linked List
Reverse a singly linked list.  

<details><summary>sol1</summary>
<p>

#### iteratively, easy. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iterative
        dummy = ListNode(0)
        while head:
            nxt = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = nxt
        return dummy.next
```
</p></details>

<details><summary>sol2</summary>
<p>

#### recursively, cool. point head.next.next = head. ex: 1-2-3, point 3's next to 2. Then modify head.next to None. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        #WOW!!
        head.next.next = head
        head.next = None
        return newHead
```
</p></details>

## 207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.  
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]  
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?  

<details><summary>sol</summary>
<p>

#### topological sort, use visited and inDegree to find the new start(with inDegree == 0). if can't find : all courses have prerequisite, GG. time=O(prerequisite^2), space=O(courses)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        used = set()
        for p in prerequisites:
            inDegree[p[0]] += 1
        while sum(inDegree) > 0:
            index = -1
            for i, d in enumerate(inDegree):
                if d == 0 and i not in used:
                    index = i
                    used.add(i)
                    break
            #all course have a prerequisite, nowhere to start
            if index == -1:
                return False
            for p in prerequisites:
                if p[1] == index:
                    inDegree[p[0]] -= 1
        return True
```
</p></details>

## 208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods. 

<details><summary>sol</summary>
<p>

#### a TrieNode instance should contain: children(a dictionary where key=letter, value=TrieNode), isEnd(bool). space=O(26^maxlen), time=O(len) for each operation.

</p></details>

<details><summary>code</summary>
<p>

```python
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isEnd
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
```
</p></details>

## 209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.  

<details><summary>sol</summary>
<p>

#### 2 pointers left and right, time=O(n), space=O(1). // sol2 : binary search, time=O(nlogn), space=O(n), use a list to record the accumulative sum, not implemented

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0
        left = right = 0
        res = float('inf')
        cur_sum = nums[0]
        while left < len(nums):
            # WA: Be careful with the right upper bound
            while cur_sum < s and right < len(nums)-1:
                right += 1
                cur_sum += nums[right]
            if cur_sum >= s:
                res = min(res, right-left+1)
            left += 1
            cur_sum -= nums[left-1]
        return res
```
</p></details>

## 210. Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n-1.  
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]  
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.  
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.  

<details><summary>sol</summary>
<p>

#### topological sort, time=O(E+V), space=O(E+V), use a stack of inDegree == 0 to select next one.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # topological sort
        inDegree = [0] * numCourses
        neighbors = {}
        zero_inDegree = []
        res = []
        for p in prerequisites:
            inDegree[p[0]] += 1
            neighbors[p[1]] = neighbors.get(p[1], []) + [p[0]]
        for i, d in enumerate(inDegree):
            if d == 0:
                zero_inDegree.append(i)
        while zero_inDegree:
            cur = zero_inDegree.pop()
            res.append(cur)
            if cur in neighbors:
                for n in neighbors[cur]:
                    inDegree[n] -= 1
                    if inDegree[n] == 0:
                        zero_inDegree.append(n)
        return res if len(res) == numCourses else []
```
</p></details>

<details><summary>sol2</summary>
<p>

#### DFS, time=O(V+E), space=O(V+E), build the adjacency matrix, dfs the white nodes, meet grey nodes during DFS->cycle.

</p></details>

<details><summary>code</summary>
<p>

```python
def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # dfs
        adj_list = {}
        for dst, src in prerequisites:
            adj_list[src] = adj_list.get(src, []) + [dst]
        # white:0, grey:1, black:2
        color = [0] * numCourses
        self.possible = True
        self.res = []
        def dfs(node):
            if not self.possible:
                return
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 1
                        dfs(neighbor)
                    elif color[neighbor] == 1:
                        # exist cycle
                        self.possible = False
                        return
            color[node] = 2
            self.res = [node] + self.res
            return
        for node in range(numCourses):
            if color[node] == 0:
                dfs(node)
        return self.res if self.possible else []
```
</p></details>
