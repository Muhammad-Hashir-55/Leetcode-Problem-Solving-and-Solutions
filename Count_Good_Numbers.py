class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        if(n %2 ==0):
            ne = n//2
        else:
            ne =(n+1)//2
        no = n//2
        total_e = pow(5,ne,m) # all possible combinations for even indices
        total_o = pow(4,no,m) # all possible combinations for odd indices
        return (total_e * total_o) % m
        
