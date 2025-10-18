class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last_picked = -10**18
        uniq = 0
        for i in nums:
            lowb = i-k
            upb = i+k
            if(last_picked < lowb):
                last_picked = lowb
            else:
                last_picked +=1
            if(last_picked <=upb):
                uniq +=1
            else:
                last_picked -=1
        return uniq
        
        
