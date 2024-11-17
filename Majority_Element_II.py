class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nn = n//3
        freq = {}
        for i in nums:
            if(i in freq):
                freq[i] +=1
            else:
                freq[i]= 1
        ans = []
        for j in freq:
            if(freq[j]>nn):
                ans.append(j)
        return ans
        
