class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        n = len(s)
        idx = n-1
        tot = 0
        curr = ''
        arr = []
        while(idx >=0):
            if(s[idx] == '-'):
                idx -=1
            else:
                curr += s[idx]
                idx -=1
                tot +=1
                if(tot == k):
                    arr.append(curr)
                    tot = 0
                    curr = ''
        if(curr):
            arr.append(curr)
        fin_arr = []
        for i in arr:
            x = i[::-1]
            fin_arr.append(x)
        fin_arr = fin_arr[::-1]
        return ('-').join(fin_arr)
        




        
