class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lis = []
        n = len(number)
        for i in range(n):
            if(number[i] ==digit):
                s = number[:i] + number[i+1:]
                lis.append(s)
        maxi = lis[0]
        for j in lis[1:]:
            if(int(j)>int(maxi)):
                maxi = j
        return maxi
        
