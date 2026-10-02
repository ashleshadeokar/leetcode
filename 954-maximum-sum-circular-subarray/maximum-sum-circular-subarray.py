class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        Max, Min = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            Max = max(Max, curMax)
            Min = min(Min, curMin)

        if Max < 0:
            return Max

        return max(Max, total - Min)