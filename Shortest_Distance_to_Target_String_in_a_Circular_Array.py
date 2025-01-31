class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if(target not in words):
            return -1
        i1 = 0
        i2 = 0
        c1 = False
        c2 = False
        ii = startIndex
        n = len(words)

        while(c1 ==False):
            if(words[ii] == target):
                c1= True
                break
            ii +=1
            ii = ii %n
            i1 +=1
        
        ii = startIndex

        while(c2 ==False):
            if(words[ii] == target):
                c2= True
                break
            ii -=1
            i2+=1
        return min(i1,i2)

        

        
