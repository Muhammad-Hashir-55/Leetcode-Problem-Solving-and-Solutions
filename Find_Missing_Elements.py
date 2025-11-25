class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        ss = set(nums)
        arr= []
        for i in range(mini,maxi+1):
            if(i not in ss):
                arr.append(i)
        return arr

        
