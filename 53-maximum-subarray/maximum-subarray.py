class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]
        # curSum = 0
        # for n in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += n
        #     res = max(curSum,res)
        # return res

        # Divide and Conquer
        def dfs(l, r):
            if l > r:
                return float("-inf")
            
            leftSum = rightSum = curSum = 0
            m = l + r >> 1
            for i in range(m - 1, l - 1, -1):
                curSum += nums[i]
                leftSum = max(curSum, leftSum)
            
            curSum = 0
            for i in range(m + 1, r + 1):
                curSum += nums[i]
                rightSum = max(curSum, rightSum)

            return (max(dfs(l, m - 1), dfs(m + 1, r), leftSum + nums[m] + rightSum))
        return dfs(0, len(nums) - 1)