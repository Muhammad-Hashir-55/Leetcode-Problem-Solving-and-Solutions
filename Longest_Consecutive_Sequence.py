class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        longest = 0
        for i in ss:
            if((i-1) not in ss):
                curr_s = 1
                curr= i
                while((curr + 1) in ss):
                    curr_s +=1
                    curr +=1
                longest = max(longest,curr_s)
        return longest
        
