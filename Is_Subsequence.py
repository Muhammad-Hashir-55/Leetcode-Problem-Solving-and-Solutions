class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) ==0):
            return True
        s_index = 0
        t_index = 0
        while(t_index <len(t)):
            if(s_index <len(s) and s[s_index] == t[t_index]):
                s_index = s_index +1
            t_index = t_index +1
        if(s_index == len(s)):
            return True
        else:
            return False