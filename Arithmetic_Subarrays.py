class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        m  = len(l)
        arr = []
        for i in range(m):
            x = nums[l[i]:r[i]+1]
            x.sort()
            nn = len(x)
            diff = x[1] - x[0]
            c = True
            for j in range(1,nn):
                if(x[j]- x[j-1]!= diff):
                    c = False
                    break
            
            if(c == True):
                arr.append(True)
            else:
                arr.append(False)
        return arr
        

        
