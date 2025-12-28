class Solution:
    def concatHex36(self, n: int) -> str:
        nn = n**2
        nnn = n**3
        s1 = ''
        s1 = hex(nn)[2:].upper()
        base_36 = ''
        alphas = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if(nnn == 0):
            return s1 + '0'
        while(nnn>0):
            rem = nnn%36
            base_36 = alphas[rem] + base_36
            nnn //= 36
        return s1 + base_36

        
