class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = False
        for i in s:
            if(i  in 'aeiou'):
                c = True
                break
        return c
        
        
        

        
