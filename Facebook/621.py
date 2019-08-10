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
    
class Solution:
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        counter = list(collections.Counter(tasks).values())
        most_frequent = max(counter)
        frequent_count = counter.count(most_frequent)
        middle = (most_frequent - 1) * (n - frequent_count + 1)
        other_tasks = len(tasks) - frequent_count * most_frequent
        idle = 0 if middle - other_tasks < 0 else middle - other_tasks
        return idle + len(tasks)
        
