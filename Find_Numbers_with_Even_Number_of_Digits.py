class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_digits = 0
        count = 0
        our_digits = [1,2,3,4,5,6,7,8,9,0]
        for i in nums:
            if(i in our_digits):
                continue
            count = 0
            result = i
            while(result!=0):
                result = result //10
                count = count +1
            if(count%2 == 0):
                even_digits = even_digits + 1
        return even_digits

        
