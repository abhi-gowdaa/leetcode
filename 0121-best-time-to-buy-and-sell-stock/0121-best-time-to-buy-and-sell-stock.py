#brute force O(N^2)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxp=0
#         buy=0
#         n=len(prices)
#         for i in range(n):
#             for j in range(i,n-1):
#                 if prices[j+1] > prices[i]:
#                     profit=(prices[j+1] - prices[i])
#                     maxp=max(maxp,profit)
#         return maxp
    
#optimized O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice=price
        
            profit=price-minprice
    
            if profit > maxprofit:
                maxprofit=profit
        
        return maxprofit

