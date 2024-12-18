class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        arr = []
        for i in range(1,1000):
            arr.append(n*i)
            if(arr[-1]%2 ==0):
                return arr[-1]
        
