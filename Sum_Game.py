class Solution:
    def sumGame(self, num: str) -> bool:
        
        n = len(num)
        half = n//2
        sumi1 = 0
        sumi2 = 0
        count1 = 0
        count2 = 0
        for i in range(half):
            if(num[i] == '?'):
                count1 +=1
                continue
            sumi1 += int(num[i])
        
        for i in range(half,n):
            if(num[i] == '?'):
                count2 += 1
                continue
            sumi2 += int(num[i])
        f = count1 + count2
        if(f %2 != 0):
            return True
        tar = ((count2- count1) *9)/2
        diff = (sumi1 - sumi2)
        if(diff != tar):
            return True
        else:
            return False
        


        
