class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr = nums[:k]
        n = len(nums)
        sumi = sum(arr)
        maxi = sumi/k
        for i in range(k,n):
            x = arr.pop(0)
            arr.append(nums[i])
            sumi -=x
            sumi += nums[i]
            maxi = max(maxi,sumi/k)
        return maxi
        
