class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        new_list = []
        new_string = ""
        for i in nums:
            new_string = new_string + str(i)
            n = int(new_string,2)
            if(n %5 ==0):
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
        
