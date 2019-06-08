class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # DFS
        visited = [[False] * len(rooms[0]) for i in range(len(rooms))]
        def dfs(i, j, distance):
            if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
                return
            if visited[i][j]:
                return
            if rooms[i][j] <= 0 and distance > 0 :
                return
            rooms[i][j] = min(rooms[i][j], distance)
            visited[i][j] = True
            for di, dj in (1,0), (0,1), (-1,0), (0,-1):
                dfs(i+di, j+dj, distance+1)
            visited[i][j] = False
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # BFS
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, distance = queue.pop(0)
            for I, J in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                # if I, J valid and it's an empty room
                if I >= 0 and I < len(rooms) and J >=0 and J < len(rooms[0]) and rooms[I][J] == (2**31) - 1:
                    rooms[I][J] = distance + 1
                    queue.append((I, J, distance + 1))
