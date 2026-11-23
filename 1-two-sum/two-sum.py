class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        copy = []
        for i, num in enumerate(nums):
            copy.append([num, i])

        copy.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            curr_sum = copy[i][0] + copy[j][0]
            if curr_sum == target:
                return [min(copy[i][1], copy[j][1]), max(copy[i][1], copy[j][1])]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
        return []