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
