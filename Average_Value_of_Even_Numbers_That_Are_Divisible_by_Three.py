class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr =[]
        for i in nums:
            if(i %2 ==0 and i%3 ==0):
                arr.append(i)
        sumi = sum(arr)
        if(not arr):
            return 0
        return int(sumi/len(arr))
        
