class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res
        perf = [0] * n
        suff = [0] * n
        perf[0] = suff[n -1] = 1
        for i in range(1, n):
            perf[i] = nums[i - 1] * perf[i - 1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):
            res[i] = perf[i] * suff[i]
        return res