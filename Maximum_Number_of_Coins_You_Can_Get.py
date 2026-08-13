class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        x = 0
        print(piles)
        k = n//3
        steps = 0

        for i in range(n-2,-1,-2):
            
            x +=piles[i]
            steps +=1
            if(steps == k):
                break
            
        return x

        
