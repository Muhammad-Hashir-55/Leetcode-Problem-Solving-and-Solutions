class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        if(n<5):
            return count
        for j in range(1,n+1):
            for k in range(j+1,n+1):
                x = j**2 + k**2
                xx = int(sqrt(x))

                
                if(xx <= n and xx *xx == x):
                    count +=2
                    

        return count
        
