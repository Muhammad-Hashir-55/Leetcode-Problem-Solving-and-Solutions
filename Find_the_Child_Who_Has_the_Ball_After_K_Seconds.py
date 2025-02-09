class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        arr = []
        for i in range(n):
            arr.append(i)
        
        i =0
        while(i <k):
            
            for j in range(n-2,-1,-1):
                arr.append(j)
            i +=1
            if(i ==k):
                break
            for j in range(1,n):
                arr.append(j)
            i +=1
            if(i ==k):
                break
        return arr[k]

        
