from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        bg = []
        for i in range(1,n+1):
            x = list(permutations(tiles,i))
            bg.append(x)
        
        ss = set()
        for i in bg:
            for j in i:
                if(j not in ss):
                    ss.add(j)
        return len(ss)


        
