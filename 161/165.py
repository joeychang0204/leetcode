class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        while len(v1) != len(v2):
            if len(v1) < len(v2):
                v1.append('0')
            else:
                v2.append('0')
        for i, _ in enumerate(v1):
            n1, n2 = int(v1[i]), int(v2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0
