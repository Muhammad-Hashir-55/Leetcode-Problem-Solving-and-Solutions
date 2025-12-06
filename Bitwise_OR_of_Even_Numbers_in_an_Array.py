class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if(i% 2 ==0):
                arr.append(i)
        if(not arr):
            return 0
        print(arr)
        res = arr[0]
        for i in arr[1:]:
            res = res | i
        return res
        
