class Solution:
    def numberOfMatches(self, n: int) -> int:
        cc = 0
        while(n != 1):
            if(n%2 ==0):
                cc += n/2
                n = n/2
            else:
                cc += (n-1)/2
                n = (n-1)/2 +1
        return int(cc)
