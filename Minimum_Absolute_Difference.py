class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff = 1000
        for i in range(len(arr)-1):
            if(abs((arr[i])-(arr[i+1]))<diff):
                diff = abs((arr[i])-(arr[i+1]))

        new_list = [] 

        for i in range(len(arr)-1):
            if(abs((arr[i])-(arr[i+1]))== diff):
                new_list.append([arr[i],arr[i+1]])
            
        return new_list
        

