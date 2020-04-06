import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = np.inf
        max_profit = 0
        sell = False
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                min_price = min(min_price,prices[i])
    #             print('price:',min_price)
                sell = True
            elif (sell==True)&(min_price<prices[i]):
                profit = prices[i]-min_price
    #             print('Profit:',profit,prices[i])
                max_profit = max(max_profit,profit)
            else:
                min_price = min(min_price,prices[i-1])
                profit = prices[i]-min_price
                max_profit = max(max_profit,profit)
        return max_profit
