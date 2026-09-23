class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, currMin = 0, math.inf

        for i in range(len(prices)):
            if prices[i] > currMin:
                profit = max(prices[i] - currMin, profit)
            
            currMin = min(prices[i], currMin)


        return profit