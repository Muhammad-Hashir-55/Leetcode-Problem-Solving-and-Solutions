class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        tot = numBottles
        emp =numBottles
        numBottles = 0
        while(emp >=numExchange):
            emp -= numExchange
            numExchange +=1
            tot +=1
            emp +=1
            
        return tot

        
