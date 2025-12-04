class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        d = directions
        if(n==1):
            return 0
        l =0
        r = n-1
        while(l<r and d[l]=='L'):
            l+=1
        while(l<r and d[r]=='R'):
            r-=1
        if(l>=r):
            return 0
        sumi = 0
        for i in range(l,r+1):
            if(d[i]!= 'S'):
                sumi +=1
        return sumi
        
