from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_point = prices[0]
        max_profit = 0
        
        for price in prices:
            #최대이익 갱신
            max_profit = max(price - min_point, max_profit)
            #저점 갱신 
            min_point = min(min_point, price)
           
        return max_profit
