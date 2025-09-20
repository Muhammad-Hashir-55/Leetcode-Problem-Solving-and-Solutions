class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sumi = 0
        temp = []
        for i in arr:
            sumi +=i
                
        n = len(arr)
        for i in range(n):
            sub = [arr[i]]
            for j in range(i+1,n):
                sub.append(arr[j])
                x = sum(sub)
                if(len(sub) % 2 != 0):
                    sumi +=x
                    
        
        return sumi
        
