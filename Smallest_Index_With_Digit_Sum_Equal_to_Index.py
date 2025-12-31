class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        arr = []
        idx = 0
        for i in nums:
            s = str(i)
            sumi = 0
            for j in s:
                sumi += int(j)
            if(sumi == idx):
                arr.append(idx)
            idx +=1
        
        if(arr):
            return arr[0]
        else:
            return -1
        
