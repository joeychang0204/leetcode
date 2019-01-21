class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        #TLE
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        l = len(gas)
        gas, cost = gas + gas, cost + cost
        for i in range(l):
            if gas[i] >= cost[i]:
                cur = 0
                for j in range(i, i + l):
                    cur += gas[j] - cost[j]
                    if cur < 0:
                        break
                if cur >= 0:
                    return i
        return -1
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, cur = 0, 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start
