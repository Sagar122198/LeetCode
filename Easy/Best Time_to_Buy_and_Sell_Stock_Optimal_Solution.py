class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        min_profit = float("inf")
        max_profit = 0
        for i in range(0,n):
            min_profit = min(prices[i] , min_profit)
            max_profit = max(max_profit , prices[i]-min_profit)
        return max_profit
