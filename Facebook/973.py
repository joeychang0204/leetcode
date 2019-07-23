class Solution:
    def kClosest(self, points, K: int):
        points.sort(key=lambda x:(x[0] * x[0] + x[1] * x[1]))
        return points[:K]
    
    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist ,point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [h[1] for h in heap]
    
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

print(Solution().kClosest3([[1,3],[-2,2],[2,-2]], 2))
