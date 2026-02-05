class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
            if(nums[i] == 0):
                arr.append(nums[i])
            elif(nums[i]>0):
                idx = (i + nums[i])%n
                arr.append(nums[idx])
            else:
                idx = i - abs(nums[i])
                if(idx >=0):
                    arr.append(nums[idx])
                else:
                    idx = abs(idx)
                    idx = idx %n
                    arr.append(nums[-idx])

        return arr
                    
                


        
