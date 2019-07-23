## 141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.  
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

<details><summary>sol</summary>
<p>

#### Floyd's slow and fast, while slow != fast, return True if out of loop. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
```
</p></details>

## 142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.  
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.  
  
Note: Do not modify the linked list.

<details><summary>sol</summary>
<p>

#### fast and slow. the distance from head to entry == from meeting to entry. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            slow = head.next
            fast = head.next.next
        else:
            return None
        while slow != fast:
            slow = slow.next
            if not fast or not fast.next:
                return None
            fast = fast.next.next
        #now fast points to the meeting point
        ptr1, ptr2 = head, slow
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
```
</p></details>

## 143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,  
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…  
You may not modify the values in the list's nodes, only nodes itself may be changed.

<details><summary>sol</summary>
<p>

#### three steps - find middle, reverse second half, reorder. case : not head or not head.next. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        prev = ListNode(0)
        prev.next = head
        fast = slow = head
        #find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        #reverse the second half
        cur = slow.next
        while cur:
            next = cur.next
            pre = prev.next
            prev.next = cur
            cur.next = pre
            slow.next = next
            cur = next
        slow, fast = head, prev
        while slow != prev:
            #1-2-4-3    1-5-2-4-3
            pnext = prev.next.next #3   3
            snext = slow.next #2    2
            slow.next = prev.next #1-4  1-5
            slow.next.next = snext #1-4-2   1-5-2
            prev.next = pnext #1-4-2-3  1-5-2-4
            slow = snext 
```
</p></details>

## 144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

<details><summary>sol1</summary>
<p>

#### recursive easy. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def dfs(node):
            if not node:
                return
            self.res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### iterative : pop the last one, append right child first. case : empty root. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
```
</p></details>

## 145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

<details><summary>sol</summary>
<p>

#### iterative : pop the last, append left first, return reversed res. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #2-4-3-1
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            
        return res[::-1]
```
</p></details>

## 146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.  
  
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.  
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.  
  
The cache is initialized with a positive capacity.  
  
Follow up:  
Could you do both operations in O(1) time complexity?  

<details><summary>sol1</summary>
<p>

#### cheating using collections.OrderedDict. get time =  put time = O(1), space=O(capacity)

</p></details>

<details><summary>code</summary>
<p>

```python
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### doubly linked list + dictionary. get time =  put time = O(1), space=O(capacity)

</p></details>

<details><summary>code</summary>
<p>

```python
class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.add(self.dict[key])
            return self.dict[key].val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            self.dict.pop(self.head.next.key)
            self.remove(self.head.next)
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        
    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node
```
</p></details>

## 147. Insertion Sort List
Sort a linked list using insertion sort.  
Algorithm of Insertion Sort:  
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.  
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.  
It repeats until no input elements remain.

<details><summary>sol</summary>
<p>

#### straight forward solution creating new linked list and find the place to insert. time=O(n^2), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        while head:
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            tmp = cur.next
            cur.next = ListNode(head.val)
            cur.next.next = tmp
            head = head.next
        return dummy.next

```
</p></details>

## 148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

<details><summary>sol</summary>
<p>

#### merge sort. use slow and fast to find the middle, cut the list into half, recursively sort the sublist and finally merge them. time=O(nlogn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = slow = prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        node1 = self.sortList(head)
        node2 = self.sortList(slow)
        
        def merge(node1, node2):
            dummy = cur = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
            if not node1:
                cur.next = node2
            if not node2:
                cur.next = node1
            return dummy.next
        return merge(node1, node2)
        

```
</p></details>

## 149. 
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

## 150. Evaluate Reversed Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.  
Valid operators are +, -, *, /. Each operand may be an integer or another expression.  
  
Note:  
Division between two integers should truncate toward zero.  
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.  

<details><summary>sol</summary>
<p>

#### stack popping the last two. case : 6/(-132) should return 0. Use eval otherwise simply dividing will return -1 in Python 2. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                else:
                    if num1 * num2 < 0:
                        stack.append(int(abs(num1)/abs(num2)) * (-1))
                    else:
                        stack.append(int(num1/num2))
            else:
                stack.append(int(t))
        return stack[-1]
```
</p></details>
