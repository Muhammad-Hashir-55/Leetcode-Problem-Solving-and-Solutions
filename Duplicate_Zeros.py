class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n  = len(arr)
        i = 0
        duplicated = False
        while(i<n):
            if(arr[i]==0 and duplicated == False):
                arr.insert(i+1,0)
                duplicated = True
                i = i +1
            else:
                duplicated = False
                i = i+1
        while(len(arr)!= n):
            arr.pop(len(arr)-1)