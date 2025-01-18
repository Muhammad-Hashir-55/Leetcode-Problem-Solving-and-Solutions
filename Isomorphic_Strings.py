class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        
        dic = {}
        for i in range(n1):
            if(s[i] not in dic):
                dic[s[i]] = t[i]
            elif(s[i] in dic and dic.get(s[i]) == t[i]):
                continue
            else:
                return False
        c1 = True

        dic = {}
        for i in range(n1):
            if(t[i] not in dic):
                dic[t[i]] = s[i]
            elif(t[i] in dic and dic.get(t[i]) == s[i]):
                continue
            else:
                return False
        c2 = True

        return c1 == c2

        
        
