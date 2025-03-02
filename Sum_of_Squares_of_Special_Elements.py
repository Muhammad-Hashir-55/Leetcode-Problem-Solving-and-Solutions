class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        arr = []
        n = len(nums)
        idx = 1
        for i in nums:
            if(n % idx == 0):
                arr.append(i)
            idx +=1
        print(arr)
        sumi = 0
        for i in arr:
            sumi = sumi + i *i
        return sumi
