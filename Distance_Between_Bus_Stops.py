class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        c1 = 0
        n = len(distance)
        
        
        
        i = start
        while(i != destination ):
            c1 += distance[i]
            i +=1
            i = i %n
        
        c2 = 0
        i = destination
        while(i != start):
            c2 += distance[i]
            i +=1
            i = i %n
        return min(c1,c2)

