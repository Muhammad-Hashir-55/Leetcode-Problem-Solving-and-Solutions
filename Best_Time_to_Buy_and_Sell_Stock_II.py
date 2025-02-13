class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        start = prices[0]
        maxi = 0
        # formula used maxi = maxi + (prices[i] - start)
        for i in range(n):
            if(start <prices[i]):
                maxi = maxi + (prices[i] - start)
            start = prices[i]
        return maxi


        
