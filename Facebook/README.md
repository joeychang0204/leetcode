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

## 125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  

Note: For the purpose of this problem, we define empty string as valid palindrome.

<details><summary>sol1</summary>
<p>

#### Use a new string to store alphanumeric. space=O(n), time=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                new_s += letter
        return new_s == new_s[::-1]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Two pointers left and right, skip the invalid characters. use str.isalnum() to check if str is alphanumeric. time=O(n), space=O(1)

<details><summary>code</summary>
<p>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        return True
```
</p></details>

## 173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.  
Calling next() will return the next smallest number in the BST.

<details><summary>sol1</summary>
<p>

#### cheating traverse all in advance. time=O(1), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node_vals = []
        self.ptr = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.node_vals.append(node.val)
            dfs(node.right)
        dfs(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.ptr += 1
        return self.node_vals[self.ptr - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.ptr < len(self.node_vals)
```
</p></details>

<details><summary>sol2</summary>
<p>

#### use a stack to store nodes, push all of the left nodes at once. In next, pop the last node and pushLeft(node.right). time=O(n) for n nodes, space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.pushLeft(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.nodes.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodes) > 0
    def pushLeft(self, node):
        while node:
            self.nodes.append(node)
            node = node.left
```
</p></details>

## 76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

<details><summary>sol</summary>
<p>

#### Sliding window with two pointers. Use two counters for the requirement and current substring. Use a variable to keep track of how many requirements we're meeting.
#### time=O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        req = collections.Counter(s2)
        s1_c = collections.defaultdict(int)
        l, r, cur = 0, 0, 0
        res = [float('inf'), 0, 0]
        while r < len(s1):
            added = s1[r]
            s1_c[added] += 1
            if added in req and s1_c[added] == req[added]:
                cur += 1
                
            while l <= r and cur == len(req):
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                prev = s1[l]
                s1_c[prev] -= 1
                if prev in req and s1_c[prev] == req[prev] - 1:
                    cur -= 1
                l += 1
            r += 1
        return s1[res[1]: res[2]+1] if res[0] != float('inf') else ''
```
</p></details>

## 304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).  

<details><summary>sol</summary>
<p>

#### The function would be called for many times, need to do preprocessing. Calculate each element's cumulative sum from (0,0), make them as the lower right corner. And then we can compute the rectangle sum in O(1).
#### initialize time = O(mn), space=O(mn). function time=O(1), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # empty matrix?
        self.lower_right = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row, cur_row in enumerate(matrix):
            row_sum = 0
            for col, num in enumerate(cur_row):
                row_sum += matrix[row][col]
                self.lower_right[row][col] += row_sum
                if row > 0:
                    self.lower_right[row][col] += self.lower_right[row - 1][col]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1 = self.lower_right[row2][col2]
        sum2 = 0 if col1 == 0 else self.lower_right[row2][col1 - 1]
        sum3 = 0 if row1 == 0 else self.lower_right[row1 - 1][col2]
        sum4 = 0 if col1 == 0 or row1 == 0 else self.lower_right[row1 - 1][col1 - 1]
        return sum1 - sum2 - sum3 + sum4
```
</p></details>

## 438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.  
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.  
The order of output does not matter.  

<details><summary>sol1</summary>
<p>

#### using two counters. Compare them everytime. 
#### time = O(n^2)??, space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = collections.Counter(s[:len(p)])
        p_counter = collections.Counter(p)
        l, r = 0, len(p) - 1
        res = []
        while r < len(s):
            if s_counter == p_counter:
                res.append(l)
            l, r = l + 1, r + 1
            if r == len(s):
                break
            if s_counter[s[l-1]] == 1:
                # Counter can also pop by key
                s_counter.pop(s[l-1])
            else:
                s_counter[s[l-1]] -= 1
            # default value of Counter is 0, can += 1 directly
            s_counter[s[r]] += 1
        return res
            
```
</p></details>

<details><summary>sol2</summary>
<p>

#### First get the required string's counter. Keep moving right pointer and update the counter. If counter[A] > 0, means it is required so missing -= 1. When moving left pointer, counter[A] >= 0 means we are discarding something required, so missing += 1.
#### time = O(n), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req = collections.Counter(p)
        l, r = 0, 0
        res = []
        missing = len(p)
        while r < len(s):
            if req[s[r]] > 0:
                missing -= 1
            req[s[r]] -= 1
            
            if missing == 0:
                res.append(l)
            if r - l + 1 == len(p):
                if req[s[l]] >= 0:
                    missing += 1
                req[s[l]] += 1
                l += 1
            r += 1
        return res

```
</p></details>

## 785. Is Graph Bipartite?
Given an undirected graph, return true if and only if it is bipartite.  
Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.  
The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

<details><summary>sol</summary>
<p>

#### DFS. All of current node's neighbors should be in the opposite set(color).
#### time = O(n), space = O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        color = {}
        def dfs(node, cur_color):
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor] == cur_color:
                        return False
                else:
                    color[neighbor] = 1 - cur_color
                    if not dfs(neighbor, 1 - cur_color):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 0):
                    return False
        return True
```
</p></details>

## 680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

<details><summary>sol</summary>
<p>

#### Use a seperate function to check palindrome in a range without removing.
#### time = O(n), space = O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_pali(l, r - 1) or is_pali(l+1, r)
        return True
```
</p></details>

## 124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.  
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.  



<details><summary>sol</summary>
<p>

#### Simple recursion. compare result with node.val+l+r, but return node.val+max(l, r)
#### time = O(n), space=O(H) where H is the tree's height.

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        def dfs(node):
            if not node:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            self.res = max(self.res, l + r + node.val)
            return node.val + max(l, r)
        dfs(root)
        return self.res

```
</p></details>

## 340. Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.

<details><summary>sol</summary>
<p>

#### Sliding window with two pointers left and right. Use a counter to record the substring characters.
#### time = O(n), space = O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        counter = collections.defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            counter[s[r]] += 1
            while len(counter) > k and l <= r:
                if counter[s[l]] == 1:
                    counter.pop(s[l])
                else:
                    counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
```
</p></details>

## 211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:  
void addWord(word)  
bool search(word)  
search(word) can search a literal word or a regular expression string containing only letters a-z or '.'.  
A '.' means it can represent any one letter.  

<details><summary>sol</summary>
<p>

#### trie + DFS, addWord time=O(n), where n=word's length. search time=O(m), where m is the number of trieNodes. 

</p></details>

<details><summary>code</summary>
<p>

```python
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trie_node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = trie_node()
            node = node.children[letter]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.res = False
        def search_node(node, start):
            if start == len(word):
                if node.isEnd:
                    self.res = True
                return
            letter = word[start]
            if letter == '.':
                for child in node.children.values():
                    search_node(child, start + 1)
            else:
                if letter not in node.children:
                    return
                search_node(node.children[letter],start + 1)
        search_node(self.root,  0)
        return self.res

class trie_node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
```
</p></details>

## 269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

<details><summary>sol</summary>
<p>

#### topological sort. Remember to handle all characters appeared in words.
#### preprocessing time = O(mn) where m is the length of word. topological sort time=O(V+E) where V is the letter count and E is the edge count. space = O(E)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # case: ['z', 'z']
        edges = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)
        zeroDegree = []
        # set('yuan') -> {'y', 'u', 'a', 'n'}
        all_letters = set(''.join(words))
        print(all_letters)
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            len1, len2 = len(word1), len(word2)
            # find the first different letter. Don't forget to break!
            for j in range(min(len1, len2)):
                if word1[j] != word2[j]:
                    inDegree[word2[j]] += 1
                    edges[word1[j]].append(word2[j])
                    break
        res = ''
        # find the zero degrees
        for letter in all_letters:
            if inDegree[letter] == 0:
                zeroDegree.append(letter)
        while zeroDegree:
            cur = zeroDegree.pop()
            res += cur
            for neighbor in edges[cur]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    zeroDegree.append(neighbor)
        return '' if len(res) != len(all_letters) else res
```
</p></details>

## 314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).  
If two nodes are in the same row and column, the order should be from left to right.  

<details><summary>sol</summary>
<p>

#### BFS recording x position. Can't use DFS since have to output from top to bottom. Outputing is a little tricky using sorted.
#### time = O(nlogn), space=O(n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        d = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node = queue.pop(0)
            d[node[1]].append(node[0].val)
            if node[0].left:
                queue.append((node[0].left, node[1] - 1))
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
                
        return [d[i] for i in sorted(d.keys())]

```
</p></details>

## 986. Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.  
Return the intersection of these two interval lists.  
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)  

<details><summary>sol</summary>
<p>

#### if max(start) <= min(end), append [max_start, min_end] to answer.
#### time = O(m+n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # A: [[2,5], [6,7], [9,15]]
        # B : [[3,4], [5,8], [10,13]]
        # [3,4], [5,5], [6,7], [10,13]
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            inter_A, inter_B = A[i], B[j]
            if inter_B[0] <= inter_A[1] or inter_A[0] <= inter_B[1]:
                if max(inter_A[0], inter_B[0]) <= min(inter_A[1], inter_B[1]):
                    res.append([max(inter_A[0], inter_B[0]), min(inter_A[1], inter_B[1])])
            if inter_A[1] <= inter_B[1]:
                i += 1
            else:
                j += 1
        return res
```
</p></details>

## 349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

<details><summary>sol1</summary>
<p>

#### Transform into two sets, iterate through one set and check if it's in other set.
#### time=O(m+n), space=O(m+n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        return [num for num in nums1 if num in nums2]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Built in set intersection function. set1 & set2
#### average time=O(m+n), worst time=O(m*n), space=O(m+n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
```
</p></details>

## 896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.  
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].  
Return true if and only if the given array A is monotonic.  

<details><summary>sol2</summary>
<p>

#### Using all function.
#### time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return False
        if len(A) <= 2:
            return True
        return all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1)) 
```
</p></details>

<details><summary>sol2</summary>
<p>

#### Two variables increasing and decreasing initialized as True. Iterate through the list and change to False if violating.
#### time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                decreasing = False
            if A[i] > A[i+1]:
                increasing = False
        return increasing or decreasing
```
</p></details>

## 825. Friends Of Appropriate Ages
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.  
Person A will NOT friend request person B (B != A) if any of the following conditions are true:  
age[B] <= 0.5 * age[A] + 7  
age[B] > age[A]  
age[B] > 100 && age[A] < 100  
Otherwise, A will friend request B.  
Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.  
How many total friend requests are made?  



<details><summary>sol</summary>
<p>

#### Ask: what's the age range? 
#### Use counter for ages. Remember people don't add themselves.
#### time=O(120*120), space=O(120)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)
        res = 0
        for age1 in c:
            for age2 in c:
                if age2 > age1 or age2 <= age1 * 0.5 + 7:
                    continue
                res += c[age1] * c[age2]
                # people don't request themselves
                if age1 == age2:
                    res -= c[age1]
        return res
        
        
```
</p></details>

## 15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.  
Note:  
The solution set must not contain duplicate triplets.  

<details><summary>sol</summary>
<p>

#### sort first. use ith element as the first number, perform 2Sum in its right. Repeating nums are annoying. Each i’th num has to compare with the previous one. Continue if they're the same.
#### time=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(i, j, target):
            ans = []
            while i < j:
                cur = nums[i] + nums[j]
                if cur == target:
                    ans.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                        i += 1
                    while j < len(nums)-1 and j > 0 and nums[j] == nums[j+1]:
                        j -= 1
                elif cur < target:
                    i += 1
                else:
                    j -= 1
            return ans
        
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            ans = twoSum(i+1, len(nums)-1, -num)
            for a in ans:
                res.append([nums[i], a[0], a[1]])
        return res

```
</p></details>

## 31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.  
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).  
The replacement must be in-place and use only constant extra memory.  

<details><summary>sol</summary>
<p>

#### Start from the end of the list, find the first element which is smaller than its next. Second, from its next to the end, find the smallest number which is bigger than the element. Swap the element with the it, and then reverse the rest of the list.
#### time = O(n), space = O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #12431 -> 13122
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        less_than_next = len(nums) - 2
        while less_than_next >= 0:
            if nums[less_than_next] < nums[less_than_next+1]:
                break
            less_than_next -= 1
        if less_than_next == -1:
            # reverse-sorted
            reverse(0, len(nums)-1)
        else:
            i = len(nums)-1
            while i > less_than_next:
                if nums[i] > nums[less_than_next]:
                    break
                i -= 1
            nums[i], nums[less_than_next] = nums[less_than_next], nums[i]
            reverse(less_than_next+1, len(nums)-1)
```
</p></details>

## 98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).  
Assume a BST is defined as follows:  
The left subtree of a node contains only nodes with keys less than the node's key.  
The right subtree of a node contains only nodes with keys greater than the node's key.  
Both the left and right subtrees must also be binary search trees.

<details><summary>sol1</summary>
<p>

#### in order traversal of BST should output sorted nums.
#### time=O(n), space=O(h)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        self.res = True
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev != None:
                if self.prev >= node.val:
                    self.res = False
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.res
```
</p></details>

<details><summary>sol12</summary>
<p>

#### iterative
#### time=O(n), space=O(h)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if prev != None and prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True
```
</p></details>

## 199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.  

<details><summary>sol1</summary>
<p>

#### DFS. right first.
#### time=O(n), space=O(h)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node, level):
            if not node:
                return
            if level > len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 1)
        return res
```
</p></details>

<details><summary>sol2</summary>
<p>

#### BFS. right first.
#### time=O(n), space=O(n) (complete binary tree size=0.5n)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if level > len(res):
                res.append(node.val)
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
        return res
```
</p></details>

## 56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

<details><summary>sol</summary>
<p>

#### sort first. compare res[-1]'s end and interval's start. 
#### time=O(nlogn), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                end_time = res[-1][1]
                if interval[0] > end_time:
                    res.append(interval)
                else:
                    res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
        return res
```
</p></details>

## 133. Clone Graph
Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.

<details><summary>sol</summary>
<p>

#### case : is there node pointing to itself? is there repeated edges?
#### use a global dictionary to store nodes. solve it recursively. create the new node first before visiting the neighbors.
#### time=O(nm) where m is the number of edges, space=O(nm)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def __init__(self):
        self.nodes = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node.val in self.nodes:
            return self.nodes[node.val]
        new_neighbors = []
        # have to create object first, otherwise will have recursion loop between neighbors
        new_node = Node(node.val, [])
        self.nodes[node.val] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        return new_node

```
</p></details>

<details><summary>sol2</summary>
<p>

#### Python built-in copy library
#### time=O(nm) where m is the number of edges, space=O(nm)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        import copy
        return copy.deepcopy(node)

```
</p></details>

## 157. Read N Characters Given Read4
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

<details><summary>sol</summary>
<p>

#### use read4 to load data into a current buffer.
#### time=O(n), space=O(1)

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

## 23. Merge k Sorted Lists:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.  

<details><summary>sol</summary>
<p>

#### Use priority queue to save the first node of each list, get the node with lowest value and put the next node of it into the priority queue.  
#### test case: [], [[]], empty head in lists.
#### time = O(nlog(k)), space=O(k)

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

<details><summary>sol2</summary>
<p>

#### heapq min-heap. Note that in heapq, when there's a tie in the first value, it'll use the second value to compare. Since the ListNode class doesn't support comparing, we will get error. To solve this problem, we have to add triple(val, counter, node) into heap. So we'll use counter to compare when there's a tie.
#### time = O(nlog(k)), space=O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 2 OK solutions, 1 a bit hard solution 
        import heapq
        heap = []
        dummy = cur = ListNode(0)
        i = 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, i, head))
                i += 1
        while heap:
            cur_node = heapq.heappop(heap)[2]
            if cur_node.next:
                heapq.heappush(heap, (cur_node.next.val, i, cur_node.next))
                i += 1
            cur.next = cur_node
            cur = cur.next
        return dummy.next

```
</p></details>

## 543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.  

<details><summary>sol</summary>
<p>

#### easy recursion.
#### time=O(n), space=O(h)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def getDiameter(node):
            if not node:
                return 0
            l = getDiameter(node.left)
            r = getDiameter(node.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        getDiameter(root)
        return self.res
```
</p></details>

## 317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:  
Each 0 marks an empty land which you can pass by freely.  
Each 1 marks a building which you cannot pass through.  
Each 2 marks an obstacle which you cannot pass through.  

<details><summary>sol</summary>
<p>

#### BFS from each building, get the distance to each empty land. 
#### time=O(mn*mn) space=O(mn)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        distance = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Do BFS from each building
                if grid[i][j] == 1:
                    cur_distance = [[float('inf')] * n for _ in range(m)]
                    queue = [(i+1, j, 1), (i, j+1, 1), (i-1,j, 1), (i,j-1, 1)]
                    while queue:
                        row, col, dist = queue.pop(0)
                        if not 0 <= row < m or not 0 <= col < n:
                            continue
                        # when meeting obstacles/buildings, or revisit, continue
                        if grid[row][col] != 0 or dist >= cur_distance[row][col]:
                            continue
                        cur_distance[row][col] = dist
                        for new_row, new_col in [(row+1, col), (row-1, col), (row,col+1), (row,col-1)]:
                            queue.append((new_row, new_col, dist + 1))
                    for x in range(m):
                        for y in range(n):
                            distance[x][y] += cur_distance[x][y]
        res = float('inf')
        for x in range(m):
            for y in range(n):
                res = min(res, distance[x][y])
        return -1 if res == float('inf') else res
```
</p></details>

## 291.
description

<details><summary>sol</summary>
<p>

#### hint
#### time and space

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 291.
description

<details><summary>sol</summary>
<p>

#### hint
#### time and space

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 291.
description

<details><summary>sol</summary>
<p>

#### hint
#### time and space

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 291.
description

<details><summary>sol</summary>
<p>

#### hint
#### time and space

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>

## 291.
description

<details><summary>sol</summary>
<p>

#### hint
#### time and space

</p></details>

<details><summary>code</summary>
<p>

```python
code
```
</p></details>
