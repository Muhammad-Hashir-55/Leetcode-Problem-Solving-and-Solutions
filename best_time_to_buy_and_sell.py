class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0]
        max_profit = 0
        for i in prices:
            if(i < min_buy):
                min_buy = i
            else:
                max_profit =max(max_profit , i - min_buy)
        return max_profit 
    
    
