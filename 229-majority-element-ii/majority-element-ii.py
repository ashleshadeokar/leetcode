class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # res = set()

        # for num in nums:
        #     count = sum(1 for i in nums if i == num)
        #     if count > n // 3:
        #         res.add(num)
        # return list(res)

        nums.sort()
        res = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j - i) > n // 3:
                res.append(nums[i])
            i = j
        return res