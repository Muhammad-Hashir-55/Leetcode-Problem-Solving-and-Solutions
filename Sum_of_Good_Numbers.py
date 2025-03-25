class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(n ==1):
            return nums[0]
        arr = []
        for i in range(n):
            idx1 = i -k
            idx2 = i + k
            c1 = False
            c2 = False
            if(idx1<0):
                c1 = True
                
            if(idx2 >=n):
                c2 = True
            if(c1 and c2):
                arr.append(nums[i])
                continue
            if(c1 == False):
                if(nums[idx1]<nums[i]):
                    if(c2 == False):
                        if(nums[idx2]<nums[i]):
                            arr.append(nums[i])
                            continue
                        else:
                            continue
                    else:
                        arr.append(nums[i])
                else:
                    continue
            if(c2 == False):
                if(nums[idx2]<nums[i]):
                    if(c1 == False):
                        if(nums[idx1]<nums[i]):
                            arr.append(nums[i])
                            continue
                        else:
                            continue
                    else:
                        arr.append(nums[i])
                else:
                    continue

            
        return sum(arr)
        
