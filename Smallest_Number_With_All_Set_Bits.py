class Solution:
    def smallestNumber(self, n: int) -> int:
        power = 0
        while(True):
            num = 2**power - 1
            if(num >= n):
                return num
            power +=1
        

        
