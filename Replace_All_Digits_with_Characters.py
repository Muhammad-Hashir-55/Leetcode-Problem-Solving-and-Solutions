class Solution:
    def replaceDigits(self, s: str) -> str:
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        fin = ''
        prev = ''
        for i in s:
            if(i in alphas):
                fin +=i
                prev = i
            elif(i not in alphas):
                idx = alphas.index(prev)
                idx += int(i)
                fin +=alphas[idx]
        return fin
            
        
