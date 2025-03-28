class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2= len(s2)
        if(n1 != n2):
            return False
        if(s1 == s2):
            return True
        coun = 0
        ss =set()
        for i in range(n1):
            if(s1[i]!= s2[i]):
                coun +=1
                ss.add(s1[i])
        if(len(ss)!=2):
            return False
        for i in range(n2):
            if(s2[i]!= s1[i]):
                ss.add(s2[i])
        if(coun == 2 and len(ss)==2):
            return True
        else:
            return False
        
        
