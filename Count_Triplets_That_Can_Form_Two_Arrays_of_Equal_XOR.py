class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        coun = 0
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j,n):
                    a = prefix[i] ^ prefix[j]
                    b = prefix[j] ^ prefix[k+1]
                    
                    if(a == b):
                        coun +=1
        return coun



        
