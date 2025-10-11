class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            s = str(i)
            n = len(s)
            if(n%2 != 0):
                continue
            else:
                mid = n//2
                x1 = s[:mid]
                x2 = s[mid:]
                sumi1 = 0
                sumi2 = 0
                nn = len(x1)
                for j in range(nn):
                    sumi1 += int(x1[j])
                    sumi2 += int(x2[j])
                if(sumi1 == sumi2):
                    count +=1
        return count

        
