class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        a[0] = [1], a[1] = [2], a[2] = a[0] + a[a[0]]
        """
        inDegree = [0] * numCourses
        visited = [False] * numCourses
        for prerequisite in prerequisites:
            inDegree[prerequisite[0]] += 1
        while sum(inDegree) > 0:
            head = -1
            for i, degree in enumerate(inDegree):
                if degree == 0 and not visited[i]:
                    visited[i] = True
                    head = i
                    break
            #all course have a prerequisite, nowhere to start
            if head == -1:
                return False
            for prerequisite in prerequisites:
                if prerequisite[1] == head:
                    inDegree[prerequisite[0]] -= 1
        return True

print(Solution().canFinish(4,
[[0,1],[2,3],[1,2],[3,0]]))
