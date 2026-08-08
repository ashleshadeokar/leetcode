class Solution:
    # def is_perfect(x,y):
    #     if min(abs(x-y), abs(x+y)) > min(abs(x), abs(y)):
    #         return False
    #     if max(abs(x-y), abs(x+y)) < max(abs(x), abs(y)):
    #         return False
    #     return True

    # def perfectPairs(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         if is_perfect(arr[i], arr[i+1]):
    #             res += 1
    #     return res

    def perfectPairs(self, nums: List[int]) -> int:
        a = sorted(abs(x) for x in nums)

        ans, left = 0, 0
        for right in range(len(a)):
            while a[right] > 2 * a[left]:
                left += 1

            ans += right - left
        return ans
