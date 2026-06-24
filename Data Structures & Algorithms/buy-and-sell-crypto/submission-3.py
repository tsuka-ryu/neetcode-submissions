class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                res = prices[r] - prices[l]
                maxP = max(maxP, res)
            else:
                l = r
        return maxP
