class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        final_l = n//k
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        final_s = ''

        idx = 0
        idxx =0
        while(idxx < final_l):
            i = 0
            ss = ''
            while(i < k):
                ss += s[idx]
                i +=1
                idx +=1
            idxx +=1
           
            sumi = 0
            for j in ss:
                sumi += alphas.index(j)
            final_s += alphas[sumi % 26]
          
            

        return final_s
            



