class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        checking = False
        for i in t:
            if (i in s and (len(s) == len(t)) and s.count(i) == t.count(i)):
                checking = True
                
            else:
                return False
        return checking
    
check = Solution()
print(check.isAnagram("hi","ih"))
