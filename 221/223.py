class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rec1 = abs((C-A) * (D-B))
        rec2 = abs((G-E) * (H-F))
        x_overlap = min(C, G) - max(A, E)
        y_overlap = min(D, H) - max(B, F)
        if x_overlap<=0 or y_overlap<=0:
            return rec1+rec2
        return rec1 + rec2 - (x_overlap * y_overlap)
