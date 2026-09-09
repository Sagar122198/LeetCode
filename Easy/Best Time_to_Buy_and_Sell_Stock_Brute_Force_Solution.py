class Solution(object):
    def maxProfit(self, prices):
        # Brute Force Solution
        n = len(prices)
        profit = 0
        max_profit = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
        return max_profit
        
