class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        arr = []
        for i in queries:
            
            n = len(i)
            
            for j in dictionary:
                me = 0
                for k in range(n):
                    if(i[k] != j[k]):
                        me +=1
                if(me <=2):
                    arr.append(i)
                    break
        return arr



        
