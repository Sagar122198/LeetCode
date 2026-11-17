class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j<len(prices):
            if prices[j] - prices[i] >0:
                profit += prices[j] - prices[i]
            i +=1
            j+=1   
        return profit
