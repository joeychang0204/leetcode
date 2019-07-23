class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum, res = 0, 0
        count = collections.defaultdict(int)
        count[0] = 1
        for num in nums:
            cur_sum += num
            if cur_sum - k in count:
                res += count[cur_sum - k]
            count[cur_sum] += 1
        return res
