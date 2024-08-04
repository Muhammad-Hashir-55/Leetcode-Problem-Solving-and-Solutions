
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list = []
        if(n == 1):
            return True
        while(n != 1):
            if n in list:
                return False
            list.append(n)
            summ =0
            for i in str(n):
                summ = summ + (int(i)**2)
            n = summ
        return True
