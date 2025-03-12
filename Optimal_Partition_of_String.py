class Solution:
    def partitionString(self, s: str) -> int:
        ss = set()
        c = 0
        for i in s:
            if(i in ss):
                c +=1
                ss = set()
                ss.add(i)
                
            else:
                ss.add(i)
            
        c +=1
        
        return c
        
