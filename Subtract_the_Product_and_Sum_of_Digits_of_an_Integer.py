class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        sum =0
        product = 1
        for i in s:
            sum = sum + int(i)
            product = product * int(i)
        return product -sum
        
