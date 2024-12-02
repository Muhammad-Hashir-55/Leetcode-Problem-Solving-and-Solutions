
class Solution:
    def removeDuplicates(self, nums) -> int:
        ans = []
        ans.append(nums[0])
        n = len(nums)
        nn = len(ans)
        
        if(n == nn):
            return nn
        
        
        ans.append(nums[1])
        nn= len(ans)
        if(ans == n):
            return nn
        i = 2
        n = len(nums)
        print(ans)
        while(i<n):
            if(ans[-1]==nums[i] and ans[-2]==nums[i]):
                i= i+1
                continue
            else:
                ans.append(nums[i])
        
            i +=1
        nn = len(ans)
        while(n!= len(ans)):
            ans.append('_')
        final_n =len(ans)
        for i in range(final_n):
            nums[i] = ans[i]
        
        return nn
