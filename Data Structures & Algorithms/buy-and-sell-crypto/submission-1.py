class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = len(prices)
        while i<j:
            for k in range(i+1,j):
                profit = prices[k]-prices[i]
                max_profit = max(max_profit,profit)
            i+=1
        return max_profit