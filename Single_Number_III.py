class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        my_dict = {}
        for i in nums:
            if(i in my_dict):
                my_dict[i] +=1
            else:
                my_dict[i] = 1
        my_set= set()
        for i in my_dict:
            if(my_dict[i]==1):
                my_set.add(i)
        lis= []
        for i in my_set:
            lis.append(i)
        return lis
