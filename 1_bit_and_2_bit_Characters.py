class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        idx = 0
        while(idx < n):
            if(bits[idx] == 1):
                idx +=1
                if(idx == n-1):
                    return False
            idx +=1
        return True
        
        
