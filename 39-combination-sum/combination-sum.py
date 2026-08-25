class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
            res = []

            def cal_sum(i, cur, total):
                if total == target:
                    res.append(cur.copy())
                    return 
                if i >= len(nums) or total > target:
                    return

                cur.append(nums[i])
                cal_sum(i, cur, total + nums[i])
                cur.pop()
                cal_sum(i + 1, cur, total)

            cal_sum(0, [], 0)
            return res        