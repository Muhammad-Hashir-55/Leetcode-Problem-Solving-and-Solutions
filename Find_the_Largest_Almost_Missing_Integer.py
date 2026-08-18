class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        dic = {}
        n = len(nums)
        for i in range(n):
            x = i+k
            if(x>n):
                break
            lis = nums[i:x]
            lis = set(lis)
            
            for j in lis:
                if(j not in dic):
                    dic[j] =1
                else:
                    dic[j] +=1
        arr = []
        for i in dic:
            if(dic[i] == 1):
                arr.append(i)
        if(not arr):
            return -1
        else:
            return max(arr)

        
