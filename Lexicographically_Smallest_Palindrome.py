class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n-1
        count = 0
        k = list(s)
        while(l<r):
            if(k[l]<k[r]):
                k[r] = k[l]
                count +=1
            elif(k[r]<k[l]):
                k[l] = k[r]
                count +=1
            l +=1
            r-=1
        return ('').join(k)



        
