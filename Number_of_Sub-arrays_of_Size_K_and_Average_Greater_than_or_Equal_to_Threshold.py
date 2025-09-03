class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        coun = 0
        x = []
        sumi = 0
        for i in range(k):
            x.append(arr[i])
            sumi += arr[i]
        
        if(sumi/len(x) >= threshold):
            coun +=1

        for i in range(k,n):
            num = x.pop(0)
            sumi -= num
            x.append(arr[i])
            sumi += arr[i]
            if(len(x) == k ):
                if(sumi/len(x) >= threshold ):
                    coun +=1
        return coun

        
