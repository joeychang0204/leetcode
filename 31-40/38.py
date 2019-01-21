class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ['1']
        while len(ans) < 30:
            prev = ans[-1]
            counter, cur = 0, ''
            for i, ch in enumerate(prev):
                if i > 0 and prev[i] != prev[i-1]:
                    cur += str(counter) + prev[i-1]
                    counter = 0
                counter += 1
            cur += str(counter) + prev[-1]
            ans.append(cur)
        return ans[n-1]
                    
