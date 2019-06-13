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
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            if letter not in cur.child:
                cur.child[letter] = TrieNode()
            cur = cur.child[letter]
        cur.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        self.res = False
        def dfs(node, word):
            if self.res:
                return
            if len(word) == 0:
                if node.isEnd:
                    self.res = True
                return
            if word[0] == '.':
                for c in node.child.values():
                    dfs(c, word[1:])
            else:
                if word[0] in node.child:
                    dfs(node.child[word[0]], word[1:])
            return
        dfs(self.root, word)
        return self.res
            
        
class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isEnd = False
```
</p></details>

## 212. 
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

## 213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.  

<details><summary>sol</summary>
<p>

#### curMax and prevMax, don't use list!  two-pass house robber, for num[:-1] and num[1:], be careful with short nums. time=O(n), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums) if nums else 0
        def getProfit(nums):
            curMax, prevMax = 0, 0
            for num in nums:
                tmp = curMax
                curMax = max(prevMax+num, curMax)
                prevMax = tmp
            return curMax
        p1 = getProfit(nums[:-1])
        p2 = getProfit(nums[1:])
        return max(p1, p2)
```
</p></details>

## 214. 
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

## 215.Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.  

<details><summary>sol1</summary>
<p>

#### heapq.nlargest, time=O(nlogk), space=O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
    def findKthLargest2(self, nums, k):
        # review 1 : forgot
        return heapq.nlargest(k, nums)[-1]
```
</p></details>

<details><summary>sol2</summary>
<p>

#### similar to quicksort, use pivot, partition and select, average time=O(n), worst=O(n^2), space=O(1)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(l, r, pivot_index):
            pivot = nums[pivot_index]
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            smaller = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[smaller] = nums[smaller], nums[i]
                    smaller += 1
            nums[r], nums[smaller] = nums[smaller], nums[r]
            return smaller
        def select(l, r, target):
            # review1 : easy to forget
            
            if l == r:
                return nums[l]
            pivot_index = random.randrange(l, r)
            pivot_index = partition(l, r, pivot_index)
            print(l, r, pivot_index, nums)
            # review1 Runtime Error : remember to add return before calling select
            if pivot_index > target:
                return select(l, pivot_index-1, target)
            elif pivot_index < target:
                return select(pivot_index+1, r, target)
            else:
                return nums[pivot_index]
        res = select(0, len(nums)-1, len(nums)-k)
        return res
```
</p></details>

## 216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.  
Note:  
All numbers will be positive integers.  
The solution set must not contain duplicate combinations.  

<details><summary>sol</summary>
<p>

#### backtracking with start, easy. time=O(2^10), space=O(k)

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(cur, start):
            s = sum(cur)
            if s ==n:
                if len(cur) == k:
                    res.append(cur)
                return
            elif s > n:
                return
            for i in range(start, 10):
                backtrack(cur+[i], i+1)
        backtrack([], 1)
        return res

```
</p></details>

## 217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates.  
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  

<details><summary>sol</summary>
<p>

#### No cool solution. set, space=O(n), time=O(n) / sort, space=O(1), time=O(nlogn).

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0:
                if num == nums[i-1]:
                    return True
        return False
```
</p></details>

## 218. 
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

## 219. Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.  

<details><summary>sol</summary>
<p>

#### naive time=O(nk), TLE. sol : sliding window with a set, time=O(n), space=O(k). PS: len in python is O(1) for most of the structure, remove in set is O(1) since it's implemented by hash table

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i, num in enumerate(nums):
            if num in s:
                return True
            s.add(num)
            if len(s) > k:
                s.remove(nums[i-k]) 
        return False

```
</p></details>

## 220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.  

<details><summary>sol</summary>
<p>

#### buckets, each covers a range of (t+1). Use dictionaries to implement. For each num, check the bucket and its neighbor buckets. time=O(n), space=O(numrange/(t+1))

</p></details>

<details><summary>code</summary>
<p>

```python
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or t < 0 or k<=0:
            return False
        # deal with negative nums, although no negative num in this test case
        smallest = min(nums)
        if smallest < 0:
            for i in range(len(nums)):
                nums[i] += (-smallest)
        buckets = {}
        for i, num in enumerate(nums):
            bucket_index = num // (t+1)
            if bucket_index in buckets:
                return True
            if (bucket_index+1) in buckets and abs(buckets[bucket_index+1] - num) <= t:
                return True
            if (bucket_index-1) in buckets and abs(buckets[bucket_index-1] - num) <= t:
                return True
            buckets[bucket_index]=num
            if (i+1) > k:
                buckets.pop(nums[i-k]//(t+1))
        return False
```
</p></details>
