class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a= []
        for i in range(30):
            a.append(str(2**i))
   
        n = str(n)
        leng = len(n)
        for i in a:
            s1 = n
            s2 = i
            
            if(set(s1) == set(s2) and len(s1)==len(s2)):
                x = set(s1)
                for j in x:
                    if(s1.count(j) != s2.count(j)):
                        return False
                
                return True
        return False
        
