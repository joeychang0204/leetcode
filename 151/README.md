## 151. Reverse Words in a String
Given an input string, reverse the string word by word.

<details><summary>sol</summary>
<p>

#### split, reverse and join. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])

```
</p></details>

## 152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

<details><summary>sol</summary>
<p>

#### brute force O(n^2) TLE. Should use maxi and mini to record the maximum and minimum products. swap when num<0. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxi = mini = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxi, mini = mini, maxi
            maxi = max(maxi*num, num)
            mini = min(mini*num, num)
            res = max(res, maxi, mini)
            
        return res
```
</p></details>

## 153. Find Minimum in Rotated Sorted Array
description

<details><summary>sol1</summary>
<p>

#### find the first num < nums[0]. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        prev = nums[0]
        for num in nums:
            if num < prev:
                res = num
                break
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### binary search. compare nums[mid] with nums[0]. case: len(nums)==1, already sorted. time=O(logn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # avoiding mid out of range
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        # already sorted
        if nums[r] > nums[l]:
            return nums[l]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] < nums[0]:
                r = mid - 1
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
```
</p></details>

## 154. 
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

## 155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.  
push(x) -- Push element x onto stack.  
pop() -- Removes the element on top of the stack.  
top() -- Get the top element.  
getMin() -- Retrieve the minimum element in the stack.

<details><summary>sol1</summary>
<p>

#### push the old min value again when pushing new value <= the old min. So when the min value is popped, the next popped one is old min value. time of min=O(1), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop(-1) == self.min:
            self.min = self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
```
</p></details>

<details><summary>sol2</summary>
<p>

#### when pushing, push the difference between current value and current min. So when we’re popping a negative value, we know we need to update the min value. Have to cast to int when returning. min time=O(1), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class MinStack3(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x-self.min)
            if x < self.min:
                self.min = x
    def pop(self):
        """
        :rtype: void
        """
        cur = self.stack.pop(-1)
        if cur < 0:
            self.min = self.min - cur

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        if top > 0:
            return int(top + self.min)
        else:
            return int(self.min)
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
```
</p></details>

## 156. Binary Tree Upside Down
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

<details><summary>sol1</summary>
<p>

#### recursively getting the new root. Edit root.left.left and root.left.right. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
            
        return newRoot
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iteratively, need to record previous, the right node etc. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        prev, cur, tmp = None, root, None
        while cur:
            next = cur.left 
            cur.left = tmp  
            tmp = cur.right 
            cur.right = prev
            prev = cur 
            cur = next 
            
        return prev
```
</p></details>

## 157. Read N Characters Given Read4
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

<details><summary>sol</summary>
<p>

#### use read4 to load data into a current buffer. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        res = 0
        while True:
            b = [""] * 4
            cur = min(read4(b), n-res)
            for i in range(cur):
                buf[res] = b[i]
                res += 1
            if res == n or cur < 4:
                return res
```
</p></details>

## 158. 
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

## 159. 
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

## 160. Intersection of Two Linked List
Write a program to find the node at which the intersection of two singly linked lists begins.

<details><summary>sol1</summary>
<p>

#### count the length of both lists, in the second round, move forward for the longer list. time=O(n), space=O(1)

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
        if not headA or not headB:
            return None
        diff = 0
        pA, pB = headA, headB
        # find the length difference
        while pA or pB:
            if not pA:
                diff += 1
                pB = pB.next
            elif not pB:
                diff -= 1
                pA = pA.next
            else:
                pA, pB = pA.next, pB.next
        # move diff steps forward
        pA, pB = headA, headB
        while diff != 0:
            if diff < 0:
                pA = pA.next
                diff += 1
            elif diff > 0:
                pB = pB.next
                diff -= 1
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
```
</p></details>

<details><summary>sol2</summary>
<p>

#### when pA reaches end, direct it to headB, when pB is None point to headA. They’ll meet in the second round. (case : null head). time=O(m+n) where m and n is the length of each list. space=O(1)


</p></details>

<details><summary>code</summary>
<p>

```python
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
```
</p></details>
