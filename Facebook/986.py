class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # A: [[2,5], [6,7], [9,15]]
        # B : [[3,4], [5,8], [10,13]]
        # [3,4], [5,5], [6,7], [10,13]
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            inter_A, inter_B = A[i], B[j]
            if inter_B[0] <= inter_A[1] or inter_A[0] <= inter_B[1]:
                if max(inter_A[0], inter_B[0]) <= min(inter_A[1], inter_B[1]):
                    res.append([max(inter_A[0], inter_B[0]), min(inter_A[1], inter_B[1])])
            if inter_A[1] <= inter_B[1]:
                i += 1
            else:
                j += 1
        return res
