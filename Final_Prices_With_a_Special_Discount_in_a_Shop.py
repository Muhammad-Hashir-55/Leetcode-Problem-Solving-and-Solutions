class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if(prices[j]<=prices[i]):
                    ans.append(prices[i]-prices[j])
                    break
                if(j == n-1 and prices[j]>prices[i]):
                    ans.append(prices[i])
                    break
        ans.append(prices[-1])
        return ans
        
