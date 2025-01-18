class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        n = len(stones)
        while(True):
            x1 = max(stones)
            stones.remove(x1)
            if(not stones):
                break
            x2 = max(stones)
            stones.remove(x2)
            stones.append(x1-x2)

        return x1

        
