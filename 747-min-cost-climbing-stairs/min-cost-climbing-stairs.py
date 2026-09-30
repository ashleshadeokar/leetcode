class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # def climb(i):
        #     if i >= len(cost):
        #         return 0
        #     return cost[i] + min(climb(i + 1), climb(i + 2))
        # return min(climb(0), climb(1))

        list1 = [-1] * len(cost)
        def climb(i):
            if i >= len(cost):
                return 0
            if list1[i] != -1:
                return list1[i]
            list1[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return list1[i]
        return min(climb(0), climb(1))