class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        # return -1


        #Hash map
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return -1