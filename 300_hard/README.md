## 4. Median of two Sorted Array
There are two sorted arrays nums1 and nums2 of size m and n respectively.  
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).  
You may assume nums1 and nums2 cannot be both empty.  

<details><summary>sol0</summary>
<p>

#### cheating using statistics module. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        return statistics.median(nums1+nums2)
        
```
</p></details>

<details><summary>sol</summary>
<p>

#### first make sure one’s length greater than the other.
Second, do binary search. l=0, r=m, i = (l+r)/2, j=halfLen-i
compare A[i-1] and B[j]; compare A[i] and B[j-1] to adjust l and r. Else: (found good partition), determine the largest left and smallest right, calculate. time=O(log(min(m, n))), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n:   #make sure len(A) < len(B)
            A, B, m, n = B, A, n, m
        l, r, halfLen = 0, m, (n+m+1)/2
        while l <= r:
            i = (l+r)/2
            j = halfLen - i
            if i > 0 and A[i-1] > B[j]:
                r = i - 1
            elif i < m and A[i] < B[j-1]:
                l = i + 1
            else:   #good i partition
                if i == 0:
                    Lmax = B[j-1]
                elif j == 0:
                    Lmax = A[i-1]
                else:
                    Lmax = max(A[i-1], B[j-1])
                if (m+n)%2 == 1:
                    return Lmax
                if i == m:
                    Rmin = B[j]
                elif j == n:
                    Rmin = A[i]
                else:
                    Rmin = min(A[i], B[j])
                return (Lmax+Rmin)/2.0
```
</p></details>

## 10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.  
'.' Matches any single character.  
'*' Matches zero or more of the preceding element.  
The matching should cover the entire input string (not partial).  
Note:  
s could be empty and contains only lowercase letters a-z.  
p could be empty and contains only lowercase letters a-z, and characters like . or *.  

<details><summary>sol1</summary>
<p>

#### recursive. if p empty then s should be empty. compare the first letter in s and p. '*' indicates duplicate or just ignore it. PogChamp complexity, check leetcode.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: # if pattern is empty, str should be empty
            return not s
        firstMatch = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':  #no or lots
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:   #no *, compare first and the rest
            return firstMatch and self.isMatch(s[1:], p[1:])
```
</p></details>

<details><summary>sol2</summary>
<p>

#### DP with 2D list, iterate from the last to the front. time=O(m*n), space=O(m*n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[-1][-1] = True
        for i in range(len(p)-1, -1, -1):
            for j in range(len(s), -1, -1):
                first_match = j < len(s) and p[i] in [s[j], '.']
                if i+1 < len(p) and p[i+1] == '*':
                    dp[i][j] = dp[i+2][j] or (first_match and dp[i][j+1])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
```
</p></details>

## 23. Merge k Sorted Lists:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.  

<details><summary>sol</summary>
<p>

#### Use priority queue to save the first node of each list, get the node with lowest value and put the next node of it into the priority queue.  test case: [], [[]], empty head in lists
. time = O(nklog(k)), space=O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        head = node = ListNode(None)
        pq = PriorityQueue()
        for l in lists:
            if l:
                # (there are 2 brackets, the inner one is for tuple(key, item))
                pq.put((l.val, l))
        # while pq is not valid, will loop infinitely
        while pq.qsize()>0:
            # will delete the first item in priority queue and return the item
            cur = pq.get()[1]
            if cur.next:
                pq.put((cur.next.val, cur.next))
            node.next = cur
            node = node.next
        return head.next
```
</p></details>

## 25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.  
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.  
Example:  
Given this linked list: 1->2->3->4->5  
For k = 2, you should return: 2->1->4->3->5  
For k = 3, you should return: 3->2->1->4->5  

Note:  
Only constant extra memory is allowed.  
You may not alter the values in the list's nodes, only nodes itself may be changed.  

<details><summary>sol</summary>
<p>

#### iterative instead of recursive(not constant space). handle k nodes in a time. handle prev and nxt carefully. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def reverseKGroup2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        tail = head
        
        while True:
            count = 0
            while tail and count < k:
                tail = tail.next
                count += 1
            if count < k:
                break
            if count == k:
                nxt = tail
                for _ in range(count):
                    head_next = head.next
                    head.next = nxt
                    nxt = head
                    head = head_next
                prev.next = nxt
            head = tail
            for _ in range(count):
                prev = prev.next
        return dummy.next
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
