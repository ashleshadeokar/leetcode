class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # first = last = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i
        # return [first, last]

        def binarysearch(firstfind):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    res = m

                    if firstfind:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return res
        return [binarysearch(True), binarysearch(False)]
