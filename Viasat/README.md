## 387. First Unique Character in a String

<details><summary>sol</summary>
<p>

#### What if there's no repeating letter?
#### What can we have inside our string? ASCII? lowercase letters?->O(1) space

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        c = collections.Counter(s)
        for i, letter in enumerate(s):
            if c[letter] == 1:
                return i
        return -1
```
</p></details>

## 509. Fibonacci Number

<details><summary>sol</summary>
<p>

#### How to represent? Can I use F(0) = 0, F(1) = 1?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # O(2**N)
        
        if N < 2:
            return N
        return self.fib(N-1) + self.fib(N-2)
        
        # O(N)
        if N < 2:
            return N
        a, b = 0, 1
        n = 1
        while n < N:
            n += 1
            a, b = b, a+b
        return b
```
</p></details>

## 204. Count Primes

<details><summary>sol</summary>
<p>

#### Will there be negative input?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0], isPrime[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)
```
</p></details>

## 225. Implement Stack using Queues

<details><summary>sol</summary>
<p>

#### What queue operation can we use? (peek?)
#### O(1) pop with 2 queues / O(1) push 2 queues / O(1) pop with 1 queue

</p></details>

<details><summary>code</summary>
<p>

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            head = self.queue.pop(0)
            self.queue.append(head)
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
```
</p></details>

## 160. Intersection of Two Linked Lists

<details><summary>sol</summary>
<p>

#### What if there's no intersection?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha, hb = headA, headB
        while headA != headB:
            # move one step forward
            if headA:
                headA = headA.next
            else:
                headA = hb
            if headB:
                headB = headB.next
            else:
                headB = ha
        return headA
```
</p></details>

## 206. Reverse Linked List

<details><summary>sol</summary>
<p>

#### recursively or iteratively?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newList
```
</p></details>

## 743. Network Delay Time

<details><summary>sol</summary>
<p>

#### Directed weighted graph shortest path-> Dijkstra
#### How are the nodes labeled? What to return if we can't reach all node?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        distance = [float('inf')] * N
        visited = [False] * N
        import collections
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        distance[K-1] = 0
        while True:
            min_dist = float('inf')
            cur_node = -1
            for i in range(N):
                if distance[i] < min_dist and not visited[i]:
                    min_dist = distance[i]
                    cur_node = i
            if cur_node == -1:
                break
            visited[cur_node] = True
            for neighbor, weight in graph[cur_node]:
                distance[neighbor] = min(distance[neighbor], distance[cur_node] + weight)
        return max(distance) if max(distance) < float('inf') else -1
```
</p></details>

## 323. Number of Connected Components in an Undirected Graph

<details><summary>sol</summary>
<p>

#### How are the nodes labeled?
#### DFS or union-find

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.p = [i for i in range(n)]
        for a, b in edges:
            if self.find(a) != self.find(b):
                self.union(a, b)
        res = 0
        for i in range(n):
            if self.p[i] == i:
                res += 1
        return res
    
    def find(self, x):
        while self.p[x] != x:
            x = self.p[x]
        return x
    
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        self.p[rootb] = roota
```
</p></details>

## 50. Pow(x, n)

<details><summary>sol</summary>
<p>

#### n range? negative?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        elif n % 2 == 1:
            return x * self.myPow(x*x, n//2)
        else:
            # N % 2 == 0
            return self.myPow(x*x, n/2)

# iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n = n // 2
        return res
```
</p></details>

## 20. Valid Parentheses

<details><summary>sol</summary>
<p>

#### Other letter? empty input?

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top + ch not in ['{}', '[]', '()']:
                        return False
        return len(stack) == 0
```
</p></details>
