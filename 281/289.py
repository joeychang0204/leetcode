class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def getNext(i, j):
            neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            live = 0
            for I, J in neighbors:
                if I>=0 and I<len(board) and J>=0 and J<len(board[0]):
                    if board[I][J] >= 1:
                        live += 1
            if board[i][j] == 1:
                return 11 if (live==2 or live==3) else 10
            else:
                return -9 if live==3 else 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = getNext(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] %= 10
