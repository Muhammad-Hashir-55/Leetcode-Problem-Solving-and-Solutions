class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        if(n ==1):
            return nums[0]
        sumi = 0
        if(n %2 ==0):
            i1 = 0
            i2 = n-1
            
            for i in range(n):
                s = str(nums[i1]) + str(nums[i2])
                sumi  = sumi + int(s)
                if(i2 - i1 == 1):
                    break
                i1 +=1
                i2 -=1
        else:
            i1 = 0
            i2 = n-1
            
            for i in range(n):
                s = str(nums[i1]) + str(nums[i2])
                sumi  = sumi + int(s)
                if(i2 - i1 == 2):
                    break
                i1 +=1
                i2 -=1
            sumi += nums[i1+1]
        return sumi



        
