class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board[0]), len(board)
        surronded = [[True] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        def dfs(i, j):
            if visited[i][j]:
                return
            visited[i][j] = True
            if board[i][j] == "O":
                surronded[i][j] = False
                for k in range(4):
                    di = [1, 0, -1, 0]
                    dj = [0, 1, 0, -1]
                    if 0<=i+di[k]<=n-1 and 0<=j+dj[k]<=m-1:
                        dfs(i+di[k], j+dj[k])
            else:
                return
            
        for j in [0, n-1]:
            for i in range(m):
                dfs(j, i)
        for j in [0, m-1]:
            for i in range(n):
                dfs(i, j)
        for i in range(n):
            for j in range(m):
                if surronded[i][j]:
                    board[i][j] = "X"


        def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board[0]), len(board)
        def dfs(i, j):
            if board[i][j] == "O":
                board[i][j] = "G"
                for k in range(4):
                    di = [1, 0, -1, 0]
                    dj = [0, 1, 0, -1]
                    if 0<=i+di[k]<=n-1 and 0<=j+dj[k]<=m-1:
                        dfs(i+di[k], j+dj[k])
            else:
                return
            
        for j in [0, n-1]:
            for i in range(m):
                dfs(j, i)
        for j in [0, m-1]:
            for i in range(n):
                dfs(i, j)
        for i in range(n):
            for j in range(m):
                board[i][j] = "O" if board[i][j] == "G" else "X"
            
        
