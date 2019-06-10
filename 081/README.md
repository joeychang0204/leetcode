## 81. Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).  
You are given a target value to search. If found in the array return true, otherwise return false.

<details><summary>sol</summary>
<p>

#### binary search, but have to deal with duplicates. if nums[l] <= nums[mid] means the first half is ordered, check if nums[l] <= target <= nums[mid]. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:
                l += 1
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
```
</p></details>

## 82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

<details><summary>sol</summary>
<p>

#### If the head.val == head.next.val, we move head forward. Then we can deal with prev or prev.next. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newHead = prev = ListNode(0)
        prev.next = head
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head: # head not duplicated
                prev = prev.next
            else:
                prev.next = head.next
            head = head.next
        return newHead.next
```
</p></details>

## 83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

<details><summary>sol1</summary>
<p>

#### Similar to 82. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = tail = ListNode(0)
        tail.next = head
        tail = tail.next
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            tail.next = head.next
            head = head.next
            tail = tail.next
        return newHead.next
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Short recursive. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
```
</p></details>

## 84. 
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

## 85. 
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

## 86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.  
You should preserve the original relative order of the nodes in each of the two partitions.

<details><summary>sol</summary>
<p>

#### use two linked list less and greater to store the nodes, finally connect two lists. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        newHead = less = ListNode(0)
        gHead = greater = ListNode(0)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = gHead.next
        return newHead.next

```
</p></details>

## 87. 
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

## 88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.  
Note:  
The number of elements initialized in nums1 and nums2 are m and n respectively.  
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

<details><summary>sol</summary>
<p>

#### Compare the biggest and fill elements from the tail. time=O(n+m), space=O(1) 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n > 0:
            nums1[:n] = nums2[:n]

```
</p></details>

## 89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.  
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

<details><summary>sol</summary>
<p>

#### iteratively solve the problem. res[i] = res[i-1] + reversed(res[i-1]) + 2 ** i. ex: 0, 1, 3, 2 for i = 2 -> 0, 1, 3, 2, 6, 7, 5, 4 for i = 3. time=O(n^2), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            newRes = [(r + 2**i) for r in res]
            res = res + newRes[::-1]
        return res
```
</p></details>

## 90. Subset II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).  
Note: The solution set must not contain duplicate subsets.

<details><summary>sol</summary>
<p>

#### sort and then backtracking with start. do not backtrack for duplicates. time=O(2^n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        def backtrack(curr, start):
            self.res.append(curr)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(curr + [nums[i]], i + 1)
        backtrack([], 0)
        return self.res

```
</p></details>
