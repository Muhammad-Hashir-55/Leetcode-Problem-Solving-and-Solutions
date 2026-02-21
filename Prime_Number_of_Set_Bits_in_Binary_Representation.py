def isprime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    if(x % 2 == 0):
        return False

    for i in range(3,int(x**0.5)+1,2):
        if(x % i == 0):
            return False
    return True
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            bin_f = bin(i)
            count = bin_f.count('1')
            if(isprime(count) == True):
                ans +=1
        return ans

        
        
