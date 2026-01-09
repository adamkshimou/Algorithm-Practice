class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
           
            potential_profit = price - min_price
            
           
            max_profit = max(max_profit, potential_profit)
            
            
            if price < min_price:
                min_price = price 

        return max_profit