class Solution:
    def findSubarrays(self, nums) -> bool:
        n = len(nums)
        arr= []
        for i in range(n-1):
            
            x = []
            x.append(nums[i])
            x.append(nums[i+1])
            arr.append(x)
        nn= len(arr)
    
        for i in range(nn):
            arr[i] = sum(arr[i])
        
        dic = {}
        for i in arr:
            if(i not in dic):
                dic[i] = 1
            else:
                dic[i] +=1
    
        for i in dic:
            if(dic[i]>=2):
                return True
        return False
