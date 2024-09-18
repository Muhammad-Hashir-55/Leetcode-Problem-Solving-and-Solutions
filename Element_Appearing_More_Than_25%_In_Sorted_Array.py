class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        occur = arr.count(arr[0])
        number = arr[0]
        for i in arr:
            if(arr.count(i)>len(arr)*0.25):
                number = i
                return number
        
