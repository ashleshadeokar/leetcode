class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        r = [0] * len(prices)
        stack = []
        stack.append(0)
        for i in range(1, len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                r[index] = prices[index] - prices[i]
            stack.append(i)
        while stack:
            c = stack.pop()
            r[c] = prices[c]
        return r