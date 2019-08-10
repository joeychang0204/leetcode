## 301.Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.  
Note: The input string may contain letters other than the parentheses ( and ).  

<details><summary>sol1</summary>
<p>

#### backtracking. Maintain index, leftCount, rightCount, and the removed num while backtracking. time=O(2**N), space=O(N) where N is the number of paranthesis.

#### Can be improved by first enumerate through s to determine the left and right remains waited to be deleted. Only delete when the remain > 0.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()
        self.minRemoved = float('inf')
        def backtrack(cur_s, index, leftCount, rightCount, removed):
            if index == len(s):
                if leftCount == rightCount:
                    if removed < self.minRemoved:
                        self.res = set()
                        self.res.add(cur_s)
                        self.minRemoved = removed
                    elif removed == self.minRemoved:
                        self.res.add(cur_s)
                return
            if rightCount > leftCount or removed > self.minRemoved:
                return
            if s[index] not in '()':
                backtrack(cur_s + s[index], index+1, leftCount, rightCount, removed)
            elif s[index] == '(':
                backtrack(cur_s + s[index], index+1, leftCount+1, rightCount, removed)
                backtrack(cur_s , index+1, leftCount, rightCount, removed+1)
            else:
                backtrack(cur_s + s[index], index+1, leftCount, rightCount+1, removed)
                backtrack(cur_s , index+1, leftCount, rightCount, removed+1)
        backtrack('', 0, 0, 0, 0)
        return list(self.res)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Make use of filter. If someone in the combination pass the filter, then we can return. Else we have to update the combinations by making a set where we try to remove each parenthesis.

</p></details>

<details><summary>code</summary>
<p>

```python
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            leftCounter, rightCounter = 0, 0
            for letter in s:
                if letter == '(':
                    leftCounter += 1
                elif letter == ')':
                    rightCounter += 1
                    if rightCounter > leftCounter:
                        return False
            return leftCounter == rightCounter
        combinations = {s}
        while combinations:
            sol = list(filter(isValid, combinations))
            if sol:
                return sol
            combinations = {c[:i] + c[i+1:] for c in combinations for i in range(len(c))}
        return []
```
</p></details>

## 273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2**31 - 1.

<details><summary>sol1</summary>
<p>

#### Iterative grouping three numbers together. Be careful with the spaces. time = O(1), space=O(1)

#### Cases: 0, 1000000, 1000

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        one_to_nine = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        ten_to_nineteen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        twenty_to_ninety = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousand_to_billion = ['Thousand', 'Million', 'Billion']
        res = ''
        i = 0
        while num > 0:
            cur = num % 10
            if i % 3 == 0:
                if num % 1000 > 0 and i > 0:
                    res = thousand_to_billion[(i//3) - 1] + ' ' + res
                if (num // 10) % 10 == 1:
                    res = ten_to_nineteen[cur] + ' ' + res
                    num = num // 10
                    i += 1
                else:
                    if cur > 0:
                        res = one_to_nine[cur-1] + ' '+ res
            elif i % 3 == 1:
                if cur >= 2:
                    res = twenty_to_ninety[cur-2] + ' ' + res
            else:
                if cur > 0:
                    res = one_to_nine[cur-1] + ' Hundred ' + res
            num = num // 10
            i += 1
        return ' '.join(res.split())

```
</p></details>

<details><summary>sol2</summary>
<p>

#### Recursion. Handle cases for num==0, num<=19, num<1000, else seperately. Play with lists and join at last. time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        one_to_nineteen = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        def words(num):
            if num == 0:
                return []
            elif num <= 19:
                return [one_to_nineteen[num-1]]
            elif num < 100:
                return [tens[num//10 - 2]] + words(num % 10)
            elif num < 1000:
                return [one_to_nineteen[num//100 - 1]] + ['Hundred'] + words(num % 100)
            else:
                for i, yo in enumerate(['Thousand', 'Million', 'Billion'], 1):
                    if num < 1000 ** (i+1):
                        return words(num // (1000**i)) + [yo] + words(num % (1000**i))
        return ' '.join(words(num))
```
</p></details>

## 953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.  
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.  

<details><summary>sol</summary>
<p>

#### 1. create a dictionary order_index.  
2. reconstruct words by each word letter's index.  
3. compare the adjacent ones. (use all and zip)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {letter: i for i, letter in enumerate(order)}
        words = [[index[letter] for letter in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

```
</p></details>

## 67. Add Binary
Given two binary strings, return their sum (also a binary string).  
The input strings are both non-empty and contains only characters 1 or 0.  

<details><summary>sol1</summary>
<p>

#### One liner using built-in conversion. time=O(1)? space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
def addBinary(self, a, b):
"""
:type a: str
:type b: str
:rtype: str
"""
    return bin(int(a, 2) + int(b, 2))[2:]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Iteratively using carry and pointers. time=O(maxLen), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ptra, ptrb = len(a)-1, len(b)-1
        res = ''
        while ptra >= 0 or ptrb >= 0 or carry:
            vala = int(a[ptra]) if ptra >= 0 else 0
            valb = int(b[ptrb]) if ptrb >= 0 else 0
            res = str((vala + valb + carry) % 2) + res
            carry = (vala + valb + carry) > 1
            ptra, ptrb = ptra - 1, ptrb - 1
        return res
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
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        h = []
        rooms = 0
        for i in range(len(intervals)):
            if h and h[0] <= intervals[i][0]:
                heapq.heappop(h)
                rooms -= 1
            rooms += 1
            heapq.heappush(h, intervals[i][1])
        return rooms
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
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        rooms = 0
        sptr, eptr = 0, 0
        while sptr < len(intervals):
            if start[sptr] >= end[eptr]:
                eptr += 1
                rooms -= 1
            sptr += 1
            rooms += 1
        return rooms
```
</p></details>

## 297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.  
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.  

<details><summary>sol1</summary>
<p>

#### DFS + preorder. use recursion to deserialize. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        def dfs(node):
            if not node:
                res.append('None')
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ' '.join(res)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split()
        def reconstruct(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            node = TreeNode(l[0])
            l.pop(0)
            node.left = reconstruct(l)
            node.right = reconstruct(l)
            return node
        return reconstruct(data)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### BFS using queue. When deserializing, use a pointer of child which is initialized as 1 and increment by 1 every time. time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Codec:
    # BFS. using queue for both tasks
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res = res + ' ' + str(node.val)
            else:
                res = res + ' None'
        return res
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        data = data.split()
        root = TreeNode(int(data[0]))
        queue = [root]
        child = 1
        while queue:
            node = queue.pop(0)
            if data[child] != 'None':
                node.left = TreeNode(int(data[child]))
                queue.append(node.left)
            child += 1
            if data[child] != 'None':
                node.right = TreeNode(int(data[child]))
                queue.append(node.right)
            child += 1
            
        return root
```
</p></details>

## 973. K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).  
(Here, the distance between two points on a plane is the Euclidean distance.)  
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)  

<details><summary>sol1</summary>
<p>

#### heap. time=O(nlogK), space=O(K)

</p></details>

<details><summary>code</summary>
<p>

```python
    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist ,point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [h[1] for h in heap]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### quick select(divide and conquer). time=O(nlogK), space=O(K)

</p></details>

<details><summary>code</summary>
<p>

```python
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        
        def partition(l, r):
            pivot = dist(points[r])
            # be careful with smaller initialize
            smaller = l
            for i in range(l, r+1):
                if dist(points[i]) < pivot:
                    points[i], points[smaller] = points[smaller], points[i]
                    smaller += 1
            points[smaller], points[r] = points[r], points[smaller]
            return smaller
                
        
        l, r = 0, len(points) - 1
        while l <= r:
            if l == r:
                return points[:K]
            k = partition(l, r)
            if k > K:
                r = k - 1
            elif k < K:
                l = k + 1
            else:
                return points[:K]
```
</p></details>

## 560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

<details><summary>sol</summary>
<p>

#### Use a dictionary to record  the count of sum. Enumerate through the array, calculate the cumulative sum. If we have cur_sum - k inside the dictionary, then we add that count to the result. Finally update the dictionary.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum, res = 0, 0
        count = collections.defaultdict(int)
        count[0] = 1
        for num in nums:
            cur_sum += num
            if cur_sum - k in count:
                res += count[cur_sum - k]
            count[cur_sum] += 1
        return res

```
</p></details>

## 426. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.  
Let's take the following BST as an example, it may help you understand the problem better:  
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.  
The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.  
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.  
The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.  



<details><summary>sol</summary>
<p>

#### DFS inorder traversal. Use self.prev for the previous node, it should be the left of current node.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.head = None
        self.prev = None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not self.head:
                self.head = node
            node.left = self.prev
            # be careful with this check
            if self.prev:
                self.prev.right = node
            self.prev = node
            dfs(node.right)
        dfs(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
```
</p></details>

## 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].  
description

<details><summary>sol</summary>
<p>

#### use res to save the left product. multiply it with the right product during the second pass. extra space=O(1), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = 1
        for num in nums:
            res.append(left)
            left *= num
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = right * res[i]
            right *= nums[i]
        return res
```
</p></details>

## 721. Accounts Merge
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.  
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.  
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.  

<details><summary>sol1</summary>
<p>

#### Use a dictionary to construct email_to_accountid graph. And then dfs if not visited. time=O(sigma(aloga)) where a is the length of each account. space=O(sigma(a))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)
        visited = [False] * len(accounts)
        emails = set()
        def dfs(account):
            if visited[account]:
                return
            visited[account] = True
            for email in accounts[account][1:]:
                emails.add(email)
                for neighbor in email_to_account[email]:
                    dfs(neighbor)
        res = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            emails = set()
            dfs(i)
            res.append([account[0]] + sorted(emails))
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Union find. Need 2 dictionaries email_to_id and email_to_name. For each email, use the first email as parent and union it with the others. Finally group the emails having the same root together, output. time=O(AlogA), space=O(A)

</p></details>

<details><summary>code</summary>
<p>

```python
class disjoint_set:
    def __init__(self):
        self.parent = [i for i in range(10000)]
    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        self.parent[rootb] = roota

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        DS = disjoint_set()
        email_to_id = {}
        email_to_name = {}
        emailid = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = emailid
                    emailid += 1
                email_to_name[email] = name
                DS.union(email_to_id[account[1]], email_to_id[email])
        same_person = collections.defaultdict(list)
        for email in email_to_id:
            same_person[DS.find(email_to_id[email])].append(email)
        return [[email_to_name[person[0]]] + sorted(person) for person in same_person.values()]
```
</p></details>

## 621. Task Scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.  
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.  
You need to return the least number of intervals the CPU will take to finish all the given tasks.  

<details><summary>sol1</summary>
<p>

#### Double while loops. In the inner loop, we iterate n times and there can't be duplicate tasks in this loop. Use maximum heap to get the one we're executing. Pop it to the temp array if there are remaining tasks. time=O(n), space=O(1) since the heap and temp is very small(size <= 26)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        counter = collections.Counter(tasks)
        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        res = 0
        while max_heap:
            temp = []
            for i in range(n+1):
                if max_heap:
                    task = heapq.heappop(max_heap)
                    task += 1
                    if task < 0:
                        temp.append(task)
                res += 1
                if len(max_heap) == 0 and len(temp) == 0:
                    break
            for task in temp:
                heapq.heappush(max_heap, task)
        return res

```
</p></details>

<details><summary>sol2</summary>
<p>

#### Less code, hard idea. If we have idle count, we get the answer by returning idle + tasks_num. To get idle, consider the most frequent task(let's say it's A). If we have 3 'A's, there should be two sequences in the middle of these 3 'A's, each with a length = n. If there's some 'B' has as more as 'A's, they should fill in the middle as the same way like A. Finally, we fill the middle using other tasks with less frequency, and we get the idle. 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = list(collections.Counter(tasks).values())
        most_frequent = max(counter)
        frequent_count = counter.count(most_frequent)
        middle = (most_frequent - 1) * (n - frequent_count + 1)
        other_tasks = len(tasks) - frequent_count * most_frequent
        idle = 0 if middle - other_tasks < 0 else middle - other_tasks
        return idle + len(tasks)
        
```
</p></details>

## 158. Read N Characters Given Read4 II - Call multiple times
Too long. Check the problem here:  https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

<details><summary>sol</summary>
<p>

#### Use self.queue to store the remaining characters. Extend the characters to self.queue after loading it to buf4. Modify buf[i] directly by popping the first one in the queue.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            while self.queue and i < n:
                buf[i] = self.queue.pop(0)
                i += 1
            if i == n:
                break
            buf4 = [''] * 4
            cur_read = read4(buf4)
            self.queue.extend(buf4)
            if cur_read == 0:
                break
        return i
```
</p></details>

## 282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.  

<details><summary>sol</summary>
<p>

#### backtracking. Calculate current value while recursion, will be faster than using eval at the end. Have to remember prev_num to restore the number for multiplications. (1 + 2 * 5, 2 would be prev_num and we have to subtract it back) 

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def backtrack(index, string, value, prev_num, cur_num):
            if index == len(num):
                if value == target and cur_num == 0:
                    res.append(''.join(string[1:]))
                return
            cur_num = cur_num * 10 + int(num[index])
            str_num = str(cur_num)
            if cur_num > 0:
                backtrack(index+1, string, value, prev_num, cur_num)
            backtrack(index+1, string + ['+', str_num] , value + cur_num, cur_num, 0)
            if string:
                backtrack(index+1, string + ['-', str_num], value - cur_num, -cur_num, 0)
                backtrack(index+1, string + ['*', str_num], value - prev_num + (prev_num) * cur_num, cur_num * prev_num, 0)
        backtrack(0, [], 0, 0, 0)
        return res
```
</p></details>

## 1. 2 Sum: 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  

<details><summary>sol</summary>
<p>

#### Use dictionary. time=O(n), space=O(n)   ps: O(1) amortized lookup time since dict is implemented with hash table

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums):
            if target - num in index and index[target-num] != i:
                return [index[target-num], i]
            index[num] = i
```
</p></details>

## 278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.  
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.  
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.  



<details><summary>sol</summary>
<p>

#### binary search. time=O(logn), space=O(1). have to use mid = left + (right-left)/ 2 for other languages that will overflow.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            isBad = isBadVersion(mid)
            if isBad:
                r = mid
            else:
                l = mid + 1
        return l
```
</p></details>

## 523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.  

<details><summary>sol</summary>
<p>

#### Use dictionary to record the first appearance of cumulative_sum % k. If we have d[sum] = i and at j we have sum aggain, it means sum(nums[i+1]~nums[j]) % k == 0. So j have to > i + 1.
#### Case: k == 0, can't mod.
#### time = O(n), space = O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        # case: k==0, can't do mod!
        sums = {0:-1}
        s = 0
        for i, num in enumerate(nums):
            s = (s + num) % k if k != 0 else (s+num)
            if s in sums:
                if i - sums[s] > 1:
                    return True
            else:
                sums[s] = i
        return False
```
</p></details>

## 291.
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
