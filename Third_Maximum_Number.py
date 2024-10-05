class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        new_list = []
        for i in nums[::-1]:
            if(i not in new_list):
                new_list.append(i)
            else:
                continue
        if(len(new_list)>=3):
            return new_list[2]
        else:
            return nums[-1]
        
