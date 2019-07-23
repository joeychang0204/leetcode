class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n:   #make sure len(A) < len(B)
            A, B, m, n = B, A, n, m
        l, r, halfLen = 0, m, (n+m+1)/2
        while l <= r:
            i = (l+r)/2
            j = halfLen - i
            if i > 0 and A[i-1] > B[j]:
                r = i - 1
            elif i < m and A[i] < B[j-1]:
                l = i + 1
            else:   #good i partition
                if i == 0:
                    Lmax = B[j-1]
                elif j == 0:
                    Lmax = A[i-1]
                else:
                    Lmax = max(A[i-1], B[j-1])
                if (m+n)%2 == 1:
                    return Lmax
                if i == m:
                    Rmin = B[j]
                elif j == n:
                    Rmin = A[i]
                else:
                    Rmin = min(A[i], B[j])
                return (Lmax+Rmin)/2.0
