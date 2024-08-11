class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)>1 and (len(s) == s.count(s[0]))):
            return -1
        new_string = ""
        for i in s:
            if(s.count(i)==1):
                new_string = new_string + i
                break
        if(new_string ==""):
            return -1
        else:
            return s.index(new_string)
        