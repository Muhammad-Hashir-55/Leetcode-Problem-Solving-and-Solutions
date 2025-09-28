class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        initi = 'a'
        while(len(s) <=k):
            neww = ''
            for i in initi:
                idx = alphas.index(i)
                idx = (idx + 1) % 26
                neww += alphas[idx]
            s += neww
            initi =s
            
        
        return s[k-1]

        
