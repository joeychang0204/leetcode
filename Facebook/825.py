class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)
        res = 0
        for age1 in c:
            for age2 in c:
                if age2 > age1 or age2 <= age1 * 0.5 + 7:
                    continue
                res += c[age1] * c[age2]
                # people don't request themselves
                if age1 == age2:
                    res -= c[age1]
        return res
        
