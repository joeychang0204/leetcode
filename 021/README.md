## 21. Merge 2 Sorted Lists:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

<details><summary>sol1</summary>
<p>

#### iterative. while both not end, gogo. append the tail if there's remaining elements in one list. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return head.next
```
</p></details>

<details><summary>sol2</summary>
<p>

#### recursive. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```
</p></details>

## 22. Generate Parenthesis:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  
For example, given n = 3, a solution set is:  
[  
"((()))",  
"(()())",  
"(())()",  
"()(())",  
"()()()"  
]  

<details><summary>sol</summary>
<p>

#### DFS keeping track num of left brackets and right brackets. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def generateParenthesis(self,n):
        res = []
        def dfs(cur, l, r):
            if r > l or l > n or r > n:
                return
            if l == r and l == n:
                res.append(cur)
                return
            dfs(cur+'(', l+1, r)
            dfs(cur+')', l, r+1)
        dfs('', 0, 0)
        return res
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

## 24. Swap nodes in Pairs:
Given a linked list, swap every two adjacent nodes and return its head.

<details><summary>sol1</summary>
<p>

#### recursive. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head.next
        head.next = self.swapPairs(head.next.next)
        node.next = head
        return node
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iterative. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = prev = ListNode(0)
        res.next = prev.next = head
        while prev.next and prev.next.next:
            a, b = prev.next, prev.next.next
            a.next, b.next, prev.next = b.next, a, b
            prev = prev.next.next
        return res.next
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

## 26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.  
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

<details><summary>sol</summary>
<p>

#### Should use two pointers, modify nums[j] when seeing a new number. nums[:] = nums[:i] + nums[i+1:] can do the trick, but each of this step takes O(n) so will cause TLE. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, 0
        while i < len(nums):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
```
</p></details>

## 27. Remove element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.  
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

<details><summary>sol</summary>
<p>

#### basically same logic as 26. Use del or 2 pointers. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del(nums[i])
            else:
                i += 1
        return i
```
</p></details>

## 28. Implement Strstr()
Implement strStr().  
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  

Example 1:  
Input: haystack = "hello", needle = "ll"  
Output: 2  

Example 2:  
Input: haystack = "aaaaa", needle = "bba"  
Output: -1  

<details><summary>sol</summary>
<p>

#### Just iterate and be careful for index range. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        L = len(needle)
        for i in range(len(haystack)):
            if i + L - 1 > len(haystack) - 1:
                return -1
            if haystack[i:i+L] == needle:
                return i
        return -1
```
</p></details>

## 29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.  
Return the quotient after dividing dividend by divisor.  
The integer division should truncate toward zero.

<details><summary>sol</summary>
<p>

#### while dividend >= divisor : bit shift the divisor. time=O(logn)? space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = True
        else:
            neg = False
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            d, cur = divisor, 0
            while dividend >= d:
                d = d << 1
                cur += 1
            res += 2 ** (cur - 1)
            dividend = dividend - (d >> 1)
        if neg:
            return -res
        else:
            return res
```
</p></details>

## 30
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
