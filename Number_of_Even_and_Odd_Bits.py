class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = bin(n)[2:]
        evens = 0
        n = len(s)
        s = s[::-1]
        for i in range(0,n,2):
            if(s[i]=='1'):
                evens +=1
        odds = 0
        for i in range(1,n,2):
            if(s[i] == '1'):
                odds +=1
        return [evens,odds]
        
