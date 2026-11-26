class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # for i in range(len(nums) - 1):
        #     if nums[i] < nums[i + 1]:
        #         peak = i + 1
        #     else:
        #         peak = i
        # return peak

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m