class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        used = set()
        for p in prerequisites:
            inDegree[p[0]] += 1
        while sum(inDegree) > 0:
            index = -1
            for i, d in enumerate(inDegree):
                if d == 0 and i not in used:
                    index = i
                    used.add(i)
                    break
            #all course have a prerequisite, nowhere to start
            if index == -1:
                return False
            for p in prerequisites:
                if p[1] == index:
                    inDegree[p[0]] -= 1
        return True

print(Solution().canFinish(4,
[[0,1],[2,3],[1,2],[3,0]]))
