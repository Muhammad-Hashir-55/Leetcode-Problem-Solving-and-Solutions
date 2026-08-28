class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        n = len(plants)
        st = capacity
        for i in range(n):
            if(st >= plants[i]):
                count +=1
                st -= plants[i]
            else:
                count += i
                st = capacity
                count += (i+1)
                st -= plants[i]
        return count
                

            
        
