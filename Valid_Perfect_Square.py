class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num ==1):
            return True
        i = 2
        while(i*i<=num):
            if(num %i == 0):
                if(i == num//i):
                    return True
            i = i+1
        return False
        