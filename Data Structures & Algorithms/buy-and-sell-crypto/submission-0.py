class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = len(prices)
        profit = 0
        current_profit = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]:
                    continue
                else:
                    current_profit = prices[j] - prices[i]
                profit = max(current_profit, profit)

        return profit


        