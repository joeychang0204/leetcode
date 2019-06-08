class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        for i, cost in enumerate(costs):
            if i > 0:
                prev = costs[i-1]
                for j in range(3):
                    costs[i][j] += min(prev[(j+1)%3], prev[(j+2)%3])
        return min(costs[-1])
