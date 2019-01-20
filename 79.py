class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board[0]), len(board)
        neibors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        used = [[False]* r for i in range(c)]
        self.res = False
        def search(row, col, remains):
            used[row][col] = True
            if self.res or remains == '':
                self.res = True
                return
            for n in neibors:
                nextr, nextc = row+n[0], col+n[1]
                if nextr >= 0 and nextr < c and nextc >= 0 and nextc < r:
                    if board[nextr][nextc] == remains[0] and not used[nextr][nextc]:
                        used[nextr][nextc] = True
                        search(nextr, nextc, remains[1:])
                        used[nextr][nextc] = False
            used[row][col] = False
            return
        for i in range(c):
            for j in range(r):
                if board[i][j] == word[0]:
                    search(i, j, word[1:])
        return self.res
    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board[0]), len(board)
        used = [[False]* r for i in range(c)]
        def search(row, col, remains):
            if not remains:
                return True
            if row < 0 or row > c-1 or col < 0 or col > r-1:
                return False
            if used[row][col] or board[row][col] != remains[0]:
                return False
            used[row][col] = True
            res = search(row-1, col, remains[1:]) or search(row+1, col, remains[1:]) or search(row, col-1, remains[1:]) or search(row, col+1, remains[1:])
            used[row][col] = False
            return res
        for i in range(c):
            for j in range(r):
                if search(i, j, word):
                    return True
        return False
