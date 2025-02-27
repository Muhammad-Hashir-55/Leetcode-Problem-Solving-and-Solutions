class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        score = 0
        print(nums)
        x = [nums[0]]
        for i in range(k):
            nums[0] +=1
            x.append(nums[0])
        print(nums)
        print(x)
            
        score = sum(x[:-1])
        return score
        
