class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        arr = []
        n = len(s)

        for i in dictionary:
            nn = len(i)
            idx = 0
            idxx = 0
            ss =''
            while(idx < n and idxx < nn):
                if(s[idx] == i[idxx]):
                    ss += s[idx]
                    idxx +=1
                   
                idx +=1
            
            if(ss == i):
                arr.append(i)
        
            
        if(not arr):
            return ''
        maxi_l = -1
        for i in arr:
            x = len(i)
            if(x> maxi_l):
                maxi_l= x
        aa = []
        for i in arr:
            if(len(i) == maxi_l):
                aa.append(i)
        aa.sort()
        return aa[0]


                
        
