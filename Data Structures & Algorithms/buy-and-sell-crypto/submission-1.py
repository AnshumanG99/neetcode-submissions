class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0

        maxprofit = 0 

        while r < len(prices):
            
            profit = prices[r] - prices[l]

            if profit > maxprofit:
                maxprofit = profit

            if prices[r] < prices[l]:
                l = r

            r += 1

        return maxprofit 