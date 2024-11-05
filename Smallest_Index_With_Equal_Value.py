class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        mini = 999999999
        ii = 0
        c = False
        for i in nums:
            if(ii % 10 == i):
                c = True
                if(mini >ii):
                    c = True
                    mini = ii
            ii +=1
        if(c == False):
            return -1
        else:
            return mini


        
