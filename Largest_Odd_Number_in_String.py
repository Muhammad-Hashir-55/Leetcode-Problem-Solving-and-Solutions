class Solution:
    def largestOddNumber(self, num: str) -> str:
        if(int(num[-1]) % 2 != 0):
            return num
        
        while(int(num[-1])%2 ==0):
            if(len(num) ==1 and int(num)%2 ==0):
                return ""
            else:
                num = num[:-1]
        return num
        
        
