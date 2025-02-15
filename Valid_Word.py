class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if(n<3):
            return False
        digis = '1234567890'
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alphas1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in word:
            if( i not in digis and i not in alphas and i not in alphas1):
                return False
        
        print('passed')
        vows = 'aeiou'
        vows1 = 'AEIOU'

        cons= 'bcdfghjklmnpqrstvwxyz'
        cons1='BCDFGHJKLMNPQRSTVWXYZ'
        c1 = False

        for i in word:
            if(i in vows or i  in vows1):
                c1= True
                break
    
            
        if(c1 == False):
            return False
        c2  =False
        for i in word:
            if(i in cons or i  in cons1):
                c2 = True
                break
        if(c2 == False):
            return False
        
        return True
        
