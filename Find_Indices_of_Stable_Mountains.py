class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        indcs = []
        for i in range(1,n):
            if(height[i-1]> threshold):
                indcs.append(i)
        return indcs

        
