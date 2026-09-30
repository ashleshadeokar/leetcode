class Solution:
    def tribonacci(self, n: int) -> int:
        # dp = {}
        if n <= 2:
            return 1 if n != 0 else 0
        trib = [0, 1, 1]
        for i in range(3, n):
            tn = sum(trib)
            trib = [trib[1], trib[2], tn]

        return sum(trib)
        # if n in dp:
        #     return dp[n]
        # dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        # return dp[n]