# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         checking = False
#         for i in t:
#             if (i in s and (len(s) == len(t)) and s.count(i) == t.count(i)):
#                 checking = True
                
#             else:
#                 return False
#         return checking
    
# check = Solution()
# print(check.isAnagram("hi","ih"))



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # k1 = sorted(s)
        # k2 = sorted(t)
        # if(k1 == k2):
        #     return True
        # return False
        dic1 = {}
        n1 = len(s)
        n2 = len(t)
        if(n1 != n2):
            return False
        for i in s:
            if(i in dic1):
                dic1[i] +=1
            else:
                dic1[i] =1
        
        
        dic2 = {}

        for i in t:
            if(i in dic2):
                dic2[i] +=1
            else:
                dic2[i]= 1
        
        
        
        s1 = ''
        s2 = ''

        print(dic1,dic2)

        s = 'abcdefghijklmnopqrstuvwxyz'
        for i in s:
            if(i in dic1):
                s1  = s1 + i * dic1[i]
        
        for i in s:
            if(i in dic2):
                s2 = s2 + i * dic2[i]
        
        print(s1,s2)
        if(s1 == s2):
            return True
        else:
            return False
