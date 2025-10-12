class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        prev= nums[0]
        for i in nums[1:]:
            if(abs(i - prev) > k):
                count +=1
                prev = i
            else:
                continue
        return count
        
