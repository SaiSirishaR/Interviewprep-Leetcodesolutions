class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#prices = [7,1,5,3,6,4]
# profit - 5-1 = 4 on day 1 after you buy the stock
# profit - 3-1 = 2 on day 2 after you buy the stock
# profit - 6-1 = 5 on day 3 after you buy the stock
# profit - 4-1 = 3 on day 4 after you buy the stock

#prices = [7,8,9,3,1,4]

### 1. buy the stock, 2. sell the stock, 3. return profit

        a,b = 0,1
        total_profit = 0
        while (b < len(prices)):
          if prices[a] < prices[b]:
             profit = prices[b] - prices[a]
             total_profit = max(total_profit, profit)

          else:
              a = b

          b +=1
        return total_profit
             




           
