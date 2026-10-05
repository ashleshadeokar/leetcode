class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)

        # for num in nums:
        #     count = sum(1 for i in nums if i == num)
        #     if count > n // 2:
        #         return num

        nums.sort()
        return nums[n // 2]