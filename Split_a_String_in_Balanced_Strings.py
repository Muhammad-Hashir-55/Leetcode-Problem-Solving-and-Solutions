class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        no_of_substrings = 0
        for i in s:
            if(i =="L"):
                balance = balance +1
            else:
                balance=  balance -1
            if(balance ==0):
                no_of_substrings = no_of_substrings+1
        return no_of_substrings