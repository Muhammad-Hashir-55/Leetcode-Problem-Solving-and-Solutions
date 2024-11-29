class Solution:
    def __init__(self):
        self.ans = []
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def permu(self,nums,start,end):
        if(start == end):
            self.ans.append(nums[:])
        for i in range(start,end+1):
            self.swap(nums,start,i)
            self.permu(nums,start+1,end)
            self.swap(nums,start,i)
            
        

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        end = len(nums)-1
        start = 0
        self.permu(nums,start,end)
        final = []
        for i in self.ans:
            if (i not in final):
                final.append(i)
        return final

        
