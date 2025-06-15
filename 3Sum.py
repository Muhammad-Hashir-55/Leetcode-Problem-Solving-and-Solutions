class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = set()
        for i in range(n-2):
            f_num = nums[i]
            j = i+1
            k = n -1
            while(j<k):
                existing = f_num + nums[j] + nums[k]
                if(existing > 0):
                    k -=1
                elif(existing < 0):
                    j +=1
                else:
                    arr.add((f_num , nums[j] , nums[k]))

                    j +=1
                    k -=1
        return list(arr)

        
