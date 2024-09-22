class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        s = s[2:]
        ones = 0
        for i in s:
            if(i =='1'):
                ones +=1
        return ones
        
