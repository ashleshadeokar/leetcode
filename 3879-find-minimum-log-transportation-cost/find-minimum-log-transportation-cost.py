# class Solution:
#     def minCuttingCost(self, n: int, m: int, k: int) -> int:
#         if n <= k and m <= k:
#             return 0

#         cost = 0
#         while m > k:
#             cost += k * (m - k)
#             m = m - k

#         while n > k:
#             cost += k * (n - k)
#             n = n - k

#         return cost

class Solution(object):
    
    
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        def cal_cost(x, k):
            log_len = x - k
            cost = log_len * k
            if log_len > k:
                cost += cal_cost(log_len,k)
            return cost
    
        if m <= k and n <= k:
            cost = 0
            return cost
        elif m > k and n < k:
            cost = cal_cost(m,k)
            return cost
            
        elif n > k and m < k:
            cost = cal_cost(n,k)
            return cost
        else:
            cost = cal_cost(m,k) + cal_cost(n,k)
            return cost

# n = 5
# m = 25
# k = 10
# s = Solution()
# res = s.minCuttingCost(n,m,k)
# print (res)