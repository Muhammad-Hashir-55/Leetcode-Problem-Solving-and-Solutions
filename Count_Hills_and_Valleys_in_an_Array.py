class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        coun = 0
        skip = []
        n = len(nums)
        for i in range(1,n-1):
            if(i in skip):
                continue
            left = i
            while(left >0 and nums[left] == nums[i]):
                left -=1 
            right = i
            while(right < n-1 and nums[right] == nums[i]):
                right +=1
            if(nums[right] > nums[i] or nums[right] < nums[i]):
                for j in range(i+1,right+1):
                    if(nums[i] == nums[j]):
                        skip.append(j)
                    else:
                        break

            if(nums[left] > nums[i] and nums[right] > nums[i]  and nums[i] != nums[left] and nums[right] != nums[i]):
                coun +=1
                
                
            elif(nums[left] < nums[i] and nums[right] < nums[i]  and nums[left] != nums[i] and nums[right] != nums[i]):
                coun +=1
                
        return coun


        
