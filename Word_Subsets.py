class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        
                
        
        arr = []
        for i in words1:
            c = True
            
            for j in words2:
                for k in j:
                    if(k in i and j.count(k) <= i.count(k)):
                        continue
                    else:
                        c = False
                        break
                if(c == False):
                    break
            

            if(c == True):
                arr.append(i)
        return arr


        
