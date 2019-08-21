class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # empty matrix?
        self.lower_right = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row, cur_row in enumerate(matrix):
            row_sum = 0
            for col, num in enumerate(cur_row):
                row_sum += matrix[row][col]
                self.lower_right[row][col] += row_sum
                if row > 0:
                    self.lower_right[row][col] += self.lower_right[row - 1][col]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1 = self.lower_right[row2][col2]
        sum2 = 0 if col1 == 0 else self.lower_right[row2][col1 - 1]
        sum3 = 0 if row1 == 0 else self.lower_right[row1 - 1][col2]
        sum4 = 0 if col1 == 0 or row1 == 0 else self.lower_right[row1 - 1][col1 - 1]
        return sum1 - sum2 - sum3 + sum4
