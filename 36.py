class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch != '.':
                    seen.append((i, ch))
                    seen.append((ch, j))
                    seen.append((int(i/3), int(j/3), ch))
        return len(seen) == len(set((seen)))
