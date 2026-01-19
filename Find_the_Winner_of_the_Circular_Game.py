class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        
        k-=1
        rem =k
        while(len(arr) >1):
            arr.pop(rem)
            rem = (rem +k)%len(arr)
        return arr[0]

        
