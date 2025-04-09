class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        n = len(nums)
        for i in range(n):
            if(nums[i] in dic):
                dic[nums[i]].append(i)
                dic[nums[i]].sort()
                for j in range(len(dic[nums[i]])-1):
                    if(dic[nums[i]][j+1] - dic[nums[i]][j] <= k):
                        return True
            else:
                dic[nums[i]] = [i]
        return False
        
        
