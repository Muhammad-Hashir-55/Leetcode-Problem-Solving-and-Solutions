class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ss = set(nums)
        count =0
        for i in ss:
            x = 0
            idxs = []
            idx = 0
            for j in nums:
                if(j == i):
                    idxs.append(idx)
                    x +=1
                idx +=1
            


            if(x == 3):
                if(idxs[1]-idxs[0] == idxs[2]-idxs[1]):
                    count +=1
        return count


        
