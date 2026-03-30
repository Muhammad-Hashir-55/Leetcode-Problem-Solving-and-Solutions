class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        e1,e2,o1,o2 = [],[],[],[]
        n = len(s1)
        for i in range(n):
            if(i % 2 == 0):
                e1.append(s1[i])
                e2.append(s2[i])
            else:
                o1.append(s1[i])
                o2.append(s2[i])
        
        return sorted(e1) == sorted(e2) and sorted(o1) == sorted(o2)
        
