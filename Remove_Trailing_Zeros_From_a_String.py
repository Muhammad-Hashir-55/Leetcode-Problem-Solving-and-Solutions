class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = 0
        for i in num[::-1]:
            if(i != '0'):
                break
            idx +=1
        if(idx == 0):
            return num
        return num[:-idx]

        
