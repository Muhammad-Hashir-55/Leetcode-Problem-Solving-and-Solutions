class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            for j in range(n):
                s1 = str(i)
                s2 = str(j)
                if('0' in s1):
                    continue
                if('0' in s2):
                    continue
                if(i +j == n):
                    return [i,j]
            
        
