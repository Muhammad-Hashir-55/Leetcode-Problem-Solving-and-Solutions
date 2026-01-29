class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        bg = []
        x = []
        for i in nums:
            x.append(i)
            if(len(x) == 3):
                bg.append(x)
                x = []
        for i in bg:
            maxi = i[-1]
            mini = i[0]
            if((maxi - mini) > k):
                return []
        return bg
        
