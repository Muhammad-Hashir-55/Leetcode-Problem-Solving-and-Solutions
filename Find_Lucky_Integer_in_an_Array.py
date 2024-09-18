class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        new_list = []
        for i in arr:
            if(arr.count(i)==i):
                new_list.append(i)
        if(not new_list):
            return -1
        else:
            return max(new_list)
            
        
