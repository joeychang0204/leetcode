class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # min heap with end time
        h = []
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(h, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, intervals[i][1])
        return len(h)
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # handling start time and end time individually
        start, end = [], []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        rooms = 0
        sptr, eptr = 0, 0
        while sptr < len(intervals):
            if start[sptr] < end[eptr]:
                rooms += 1
            else:
                eptr += 1
            sptr += 1
        return rooms
                
                
                
    
                
                
                
