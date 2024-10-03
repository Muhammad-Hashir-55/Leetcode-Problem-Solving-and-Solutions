class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list =[]
        for i in nums:
            c= 0
            for j in nums:
                if(i>j):
                    c +=1
            new_list.append(c)
        return new_list
        
