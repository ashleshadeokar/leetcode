class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero, left, max_len = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1

            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len - 1
